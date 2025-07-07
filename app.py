import streamlit as st
import snscrape.modules.twitter as sntwitter

st.title("Twitter Mention Scraper")

handle = st.text_input("Enter Twitter handle (without @):", "")

if handle:
    query = f'@{handle}'
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= 10:
            break
        tweets.append(tweet.content)
    if tweets:
        st.write(f"10 most recent tweets mentioning @{handle}:")
        for idx, tweet in enumerate(tweets, 1):
            st.write(f"{idx}. {tweet}")
    else:
        st.write("No mentions found.")
