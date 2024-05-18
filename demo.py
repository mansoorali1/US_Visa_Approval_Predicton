from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

from us_visa.pipeline.training_pipeline import TrainPipeline
# below is for logging testing
#logging.info("welcome this is custom log")

# below is for exception testing ---- this can be useful when exception monitoring 
#or checking is done manually
# try:
#     a = 1 / "10"
# except Exception as e:
#     raise USvisaException(e, sys) from e

## below is for exception testing ---- this can be useful when exception is identified and issue is logged
#try:
#    a = 1 / "10"
#except Exception as e:
#    logging.info(e) ### this line helps in creating a log of the exception occurred 
#    raise USvisaException(e, sys) from e ## this line helps in raising exception which can be visible
## when script is executed or run via terminal or console

pipeline = TrainPipeline()
pipeline.run_pipeline()

                                         