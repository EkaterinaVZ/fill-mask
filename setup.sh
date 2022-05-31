mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"artprojectt@mail.ru\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\

[theme]\n\
# светлая тема\n\
primaryColor='#6eb52f'\n\
backgroundColor="#f0f0f5"\n\
secondaryBackgroundColor="#e0e0ef"\n\
textColor="#262730"\n\
font="sans serif"\n\
" > ~/.streamlit/config.toml
