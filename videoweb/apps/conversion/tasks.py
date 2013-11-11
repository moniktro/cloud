from celery import Celery
import os
import MySQLdb
from time import sleep
import time
from videoweb.settings import VIDEOS_ROOT

celery = Celery('tasks', backend='amqp', broker='amqp://')

@celery.task
def convertir(nombreOrigen, nombreDestino):


    rutaOrigen = VIDEOS_ROOT+'videos_temp/'+nombreOrigen
    rutaDestino = VIDEOS_ROOT+'videos_convertidos/'+nombreDestino

    print 'convirtiendo' + rutaDestino + '.mp4'

    conversion = 'ffmpeg -i ' +  rutaOrigen + ' -vcodec libx264 -b 250k -bt 50k -acodec libvo_aacenc -ab 56k -ac 2 -s 480x320 ' + rutaDestino + '.mp4'

    print os.system(conversion)

    os.system('rm '+rutaOrigen)
	
    # solo cambia el estado del video si este se pudo convertir
    
    print 'finalizo'

    db=MySQLdb.connect(host='localhost',user='root', passwd='cloud',db='videoweb')
    cursor=db.cursor()

    if os.path.exists(rutaDestino + '.mp4'):

        #db=MySQLdb.connect(host='localhost',user='root', passwd='cloud',db='videoweb')
        #cursor=db.cursor()
        #nombre = str(nombreDestino.replace(" ",""))

        #datepublish=str(date.strftime('%Y-%m-%d %H:%M:%S'))
        datepublish=str(time.strftime('%Y-%m-%d %H:%M:%S'))

        sql = "UPDATE appvideos_uploadvideo SET status = 1, datepublish = '%s', video = '%s' WHERE name = '%s'" % (datepublish, VIDEOS_ROOT+"videos_convertidos/"+nombreDestino+".mp4", nombreDestino)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

        return True


    else:
        sql = "DELETE FROM appvideos_uploadvideo WHERE name = '%s'" % (nombreDestino)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

        return False

        #cambiar el estado del video en la base de datos
    #db=MySQLdb.connect(host='localhost',user='root', passwd='cloud',db='videoweb')
    #cursor=db.cursor()
    #nombre = str(nombreDestino.replace(" ",""))
    
    #datepublish=str(date.strftime('%Y-%m-%d %H:%M:%S'))
    #datepublish=str(time.strftime('%Y-%m-%d %H:%M:%S'))

    #sql = "UPDATE appvideos_uploadvideo SET status = 1, datepublish = '%s', video = '%s' WHERE name = '%s'" % (datepublish, VIDEOS_ROOT+"videos_convertidos/"+nombre+".mp4", nombre)
    
    #try:
    #   cursor.execute(sql)
    #   db.commit()
    #except:
    #   db.rollback()
    #db.close()



