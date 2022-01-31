
#Nesting Dictionary in a Dictionary
```
travel_log = {
    "France": {
        "cities_visited": {
            "Paris": 2,
            "Lille": 1,
            "Dijon": 1,
        },
        "total_visits": 4,
    },
    "Germany": {
        "cities_visited": {
            "Berlin": 4,
            "Hamburg": 1,
            "Stuttgart": 2,
        },
        "total_visits": 7,
    }
}
```

#Nesting Dictionary in a List

```
travel_log = [
    {
        "country": "France",
        "cities_visited": {
            "Paris": 2,
            "Lille": 1,
            "Dijon": 1,
        },
        "total_visits": 4,
    },
        "country": "Germany",
        "cities_visited": {
            "Berlin": 4,
            "Hamburg": 1,
            "Stuttgart": 2,
        },
        "total_visits": 7,
    },
]