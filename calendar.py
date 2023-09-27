import requests
import json

BASE_URL = "https://api.teamup.com/{CALENDAR_ID}/events"
HEADERS = {
    "Teamup-Token": "{YOUR_API_TOKEN}",
    "Content-Type": "application/json"
}

# Crear evento
def create_event(title, start_date, end_date, notes=""):
    payload = {
        "title": title,
        "start_dt": start_date,
        "end_dt": end_date,
        "notes": notes
    }

    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    return response.json()

# Consultar eventos en un rango de fechas
def get_events(start_date, end_date):
    params = {
        "startDate": start_date,
        "endDate": end_date
    }

    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    return response.json()

# Editar evento
def update_event(event_id, new_title=None, new_start_date=None, new_end_date=None, new_notes=None):
    payload = {}

    if new_title:
        payload["title"] = new_title
    if new_start_date:
        payload["start_dt"] = new_start_date
    if new_end_date:
        payload["end_dt"] = new_end_date
    if new_notes:
        payload["notes"] = new_notes

    response = requests.put(f"{BASE_URL}/{event_id}", headers=HEADERS, data=json.dumps(payload))
    return response.json()

# Eliminar evento
def delete_event(event_id):
    response = requests.delete(f"{BASE_URL}/{event_id}", headers=HEADERS)
    return response.status_code

# Ejemplo de uso:
event = create_event("Test Event", "2023-09-28T10:00:00Z", "2023-09-28T12:00:00Z", "Some notes")
print(event)

events = get_events("2023-09-28", "2023-09-29")
print(events)

updated_event = update_event(event['event']['id'], new_title="Updated Test Event")
print(updated_event)

status_code = delete_event(event['event']['id'])
print(f"Delete status code: {status_code}")
