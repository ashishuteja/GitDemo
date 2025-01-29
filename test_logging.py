import logging

def test_logging():
    logger = logging.getLogger(__name__)#1
    #logging is a packege
    #getlogger is a method helps to get an object for logging feature
    #logger object is responsible for log everythong

    obj_filehandler = logging.FileHandler('logfile.log') #Filehandler knows in which file logs as to be captured.


    obj_formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s %(message)s")

    obj_filehandler.setFormatter(obj_formatter)


    logger.addHandler(obj_filehandler)#2
    #addhandler is a method, which cares what format, what file
    # #have to place filehandler object here.Filehandler is just a file location

    logger.setLevel(logging.DEBUG)
    logger.debug("Debug statement is executed")
    logger.info("Information is executed")
    logger.warning("warning message is printed")
    logger.error("error message is printed")
    logger.critical("critical message")


