import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_current_time(city: str) -> dict:
    """Retourne l'heure actuelle d'une ville donnée."""
    if city.lower() == "abidjan":
        tz_identifier = "Africa/Abidjan"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone info for {city}."
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}

root_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash",
    description="Agent qui répond aux questions d'heure locale.",
    instruction="Tu es un agent utile qui donne l'heure d'une ville.",
    tools=[get_current_time],
)
