# What is xoxzo.galib?
A simple python library to talk to Google Analytics and send hits via the Measurement Protocol

## The short version

xoxzo.galib is a simple python library to encapsulate functionality that allows you to
send specific hit types to Google Analytics using the Measurement Protocol.

## The longer version

Nearly all the time if you're thinking of talking to Google Analytics using a python library,
you'd want [Google Analytics API Client Library for Python](https://developers.google.com/api-client-library/python/apis/analytics/v3) instead.

But if all you want is a simple way to send hits of certain types to Google Analytics
from your backend in python, then maybe xoxzo.galib is for you.

These documentation was referred to when writing this library:

- https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters
- https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide

## The Details

### Required parameters

For every hit you want to send, these parameters are required:

```
    v=1             # Version.
    tid=UA-XXXXX-Y  # Tracking ID / Property ID.
    cid=555         # Anonymous Client ID.
    OR uid          # User ID
    &t=event        # Hit Type.
```

### Parameters for event hits

If you want to keep track of events such as signups, logins, downloads video plays or other
interactions done on your site, you send _event_ hits.

You can use parameters to describe a user’s interaction:

- Category (Required) is the name you give to a group of objects you want to track.
- Action (Required) – The type of interaction such as download for example
- Label (Optional) Useful for summarising what the event is about or for categorizing events (e.g. nav buttons)
- Value (Optional). If you’d like to assign a numeric value to your file download

For example, if you want to track downloads of your company brochure, you can use the parameters
like this:

- Category is "PDF"
- Action is "Download"
- Label is "Company Brochure - PDF"

Refer also to https://www.hallaminternet.com/using-google-analytics-event-tracking/ on how to use
the parameters correctly.

### Parameters for transaction hits

If you want to keep track of purchases done via your site, you send _transaction_ hits.
You can further track your purchases by sending _item_ hits: Each _item_ must be associated
with a _transaction_.

What this means is that you send one transaction hit to represent an entire transaction, 
and then send an item hit for **each item in the transaction**. The transaction ID *ti* links
all the hits together to represent the entire purchase.

Of course, you can also send a _transaction_ without any _items_ associated with it too.

```
v=1               // Version.
&tid=UA-XXXXX-Y   // Tracking ID / Property ID.
&cid=555          // Anonymous Client ID.

&t=transaction    // Transaction hit type.
&ti=12345         // transaction ID. Required.
&ta=westernWear   // Transaction affiliation.
&tr=50.00         // Transaction revenue.
&ts=32.00         // Transaction shipping.
&tt=12.00         // Transaction tax.
&cu=EUR           // Currency code.
```

## And finally.. 

This piece of software and the people writing it has nothing to do with Google, and should
be used AS IS with no applied guarantees of any kind. It's written because it helps the people
who wrote it, and hopefully it will help you too.

All copyrights are owned by their respective holders.

