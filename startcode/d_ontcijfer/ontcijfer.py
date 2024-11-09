def ontcijfer(bericht,sleutel):
    boodschap=""

    for teken in bericht:
        if teken in sleutel:
            boodschap=boodschap+teken
    return boodschap