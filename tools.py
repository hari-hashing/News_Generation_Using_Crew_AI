import os
from dotenv import load_dotenv
load_dotenv

os.environ['SERPER_API_KEY']=os.getevn('SERPER_API_KEY')

from crewai_tools import SerperDevTool

# intialization of the tool for internet ssearching capabilities
tool = SerperDevTool()
