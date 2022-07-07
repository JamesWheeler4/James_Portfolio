# Creating men's heatmap
def graphMenCor():
    df = pd.read_csv('Mens_HM_data.csv', header=None)
    df = df.values.tolist()
    fig = px.imshow(df,
                    labels=dict(x="Event x", y="Event y", color="Correlation Coefficient"),
                    x=['100m', '200m', '400m', '800m', '1500m', '3000m', 'high jump', '110m hurdles', '300m hurdles',
                       '1600m', "3200m", 'shot put', 'discus', 'javelin', 'hammer', 'pole vault', 'long jump',
                       'triple jump'],
                    y=['100m', '200m', '400m', '800m', '1500m', '3000m', 'high jump', '110m hurdles', '300m hurdles',
                       '1600m', "3200m", 'shot put', 'discus', 'javelin', 'hammer', 'pole vault', 'long jump',
                       'triple jump'],
                    text_auto=True, color_continuous_scale='balance'
                   )

    fig.update_layout(title=('Mens Highschool Track and Field Correlation Coefficient'), title_font_size=32,
                      title_x=0.5, paper_bgcolor='#f4f0e4')
    fig.show()
