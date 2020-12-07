from ics import Calendar, Event
import data

def create_eventdict(chkdict):
    n=0
    eventdict={}
    for i in chkdict:
        state=chkdict[i].get()
        if state:
            start_dd=i.find("_")
            start_service=len(i)-start_dd
            dd=i[:start_dd]
            service=i.replace(dd+"_","")
            if len(dd)==1:
                dd="0"+dd
            eventdict.update({n:{"Day":dd,"service":service}})
            print("adding "+"Day:"+dd +" Service:"+service)
            n+=1
    return eventdict


def create_events(c, yr, mon, eventdict={}):
    for event in eventdict:
        e = Event()
        eventdata = eventdict[event]
        service = eventdata["service"]
        eventday = eventdata["Day"]
        e.name = service

        eventtext = str(yr)+"-"+str(mon)+"-"+eventday+" "
        begin = eventtext+ data.begin[service]+':00'
        end = eventtext + data.end[service] + ':00'
        e.begin = begin
        e.end = end
        print("Name:"+service+" Begin:"+begin+" End:"+end)
        c.events.add(e)
    return c.events


def create_ics(chkdict, yr, mon):
    c = Calendar()
    eventdict = create_eventdict(chkdict)
    c.events = create_events(c, yr, mon, eventdict)
    c.events
    with open('my.ics', 'w') as f:
        f.write(str(c))