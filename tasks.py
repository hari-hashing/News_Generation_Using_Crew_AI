from crewai import Task 

from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate"
    "market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 4 paragraphs long report on the latest Gen AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an thoughtful article on {topic}."
    "Focus on the latest and previous trends and how it's impacting and impacted the industry."
    "article should be tech oriented , engaging, and positive."
  ),
  expected_output='A 3 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='yet_another_generated_post.txt'  # Example of output customization
)