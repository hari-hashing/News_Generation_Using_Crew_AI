import os

from crewai import Agent
from dotenv import load_dotenv
from tools import tool

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# creating a senior researcher agtent with memory and verbase mode

news_reasercher=Agent(
    role="writer",
    goal="Um{topic}",
    verbose=True,
    memory = True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    )
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

#  creating a writer agent responsible for writing news blog articles

news_writer=Agent(
    role="Writer",
    goal="narartes about ground breakign research and tech involved in {topic}  ",
    verbose=True,
    memory = True,
    backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False

)