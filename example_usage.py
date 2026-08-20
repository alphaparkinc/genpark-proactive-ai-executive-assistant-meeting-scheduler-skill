from client import ProactiveAiExecutiveAssistantMeetingSchedulerClient

def main():
    client = ProactiveAiExecutiveAssistantMeetingSchedulerClient()
    res = client.schedule_and_brief("Set up a Series B due diligence call with the VC partner next Friday afternoon")
    print("Scheduled Event:", res["scheduled_event"]["title"])
    print(f"Time: {res['scheduled_event']['start_utc']} -> {res['scheduled_event']['end_utc']}")
    print(f"Pre-Meeting Brief: {res['pre_meeting_brief']}")
    print("Suggested Agenda:")
    for item in res["suggested_agenda_items"]:
        print(f"  - {item}")

if __name__ == "__main__":
    main()
