from datetime import timedelta as td

busy = [
    {'start' : td(hours=10,minutes=30),
    'stop' : td(hours=10,minutes=50)
    },
    {'start' : td(hours=18,minutes=40),
    'stop' : td(hours=18,minutes=50)
    },
    {'start' : td(hours=14,minutes=40),
    'stop' : td(hours=15,minutes=50)
    },
    {'start' : td(hours=16,minutes=40),
    'stop' : td(hours=17,minutes=20)
    },
    {'start' : td(hours=20,minutes=5),
    'stop' : td(hours=20,minutes=20)
    }
]

start = td(
    hours=9
)
end = td(
    hours=21
)

    
def calculate_appointments(day_start: td, day_end: td, data: list[dict[str, td]], step: td = td(minutes=30)):
    data.sort(key=lambda x: x['start'])
    current_time = day_start

    appointments = [

    ]

    for e, chunk in enumerate(data):
        amount = int((chunk['start'] - current_time) / step)
        for _ in range(amount):
            s, e = current_time, current_time + step
            appointments.append({
                'start': s, 'end': e
            })
            current_time = e
        current_time = chunk['stop']

    while current_time + step < day_end:
        s, e = current_time, current_time + step
        appointments.append({
            'start': s, 'end': e
        })
        current_time = e

    return appointments
        
result = calculate_appointments(start, end, busy)

for appointment in result:
    print(f"start: {appointment['start']}; end: {appointment['end']}")

