import streamlit as st

# 1. Titolo e grafica dell'app
st.title("🎴 Conta Punti Burraco da Foto")
st.write("Carica la foto delle combinazioni sul tavolo per calcolare il punteggio totale!")

# 2. Pulsante per caricare l'immagine
uploaded_file = st.file_uploader("Scatta o seleziona la foto delle carte", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostra la foto caricata sullo schermo
    st.image(uploaded_file, caption="Foto delle carte caricata", use_container_width=True)
    
    st.info("Elaborazione dell'immagine in corso...")
    
    # Esempio simulato dei gruppi rilevati (lo collegheremo presto all'AI)
    gruppi_rilevati = {
        "Tris di Re": ['K', 'K', 'K', 'K', 'K'],
        "Tris di 6": ['6', '6', '6'],
        "Scala di Picche": ['5', '6', '7', '8', '9'],
        "Gruppo Pinella e Jack": ['2', 'J', 'J'],
        "Burraco di Quadri": ['2', '9', '10', 'J', 'Q', 'K', 'A'],
        "Gruppo in basso": ['Jolly', '7', '8']
    }
    
    # Funzione di calcolo punti
    def calcola_tutto():
        valori = {
            'Jolly': 30, '2': 20, 'A': 15,
            'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 10, '8': 10,
            '7': 5, '6': 5, '5': 5, '4': 5
        }
        
        totale_generale = 0
        st.markdown("### 📊 Dettaglio Punti per Gruppo:")
        
        for nome_gruppo, carte in gruppi_rilevati.items():
            punti_facciali = sum(valori.get(c, 0) for c in carte)
            punti_gruppo = punti_facciali
            
            # Controllo Burraco (7+ carte)
            if len(carte) >= 7:
                ha_speciali = 'Jolly' in carte or '2' in carte
                bonus = 100 if ha_speciali else 200
                punti_gruppo += bonus
                tipo_b = "Sporco" if ha_speciali else "Pulito"
                st.write(f"- **{nome_gruppo}** ({len(carte)} carte): {punti_facciali} punti + {bonus} (Burraco {tipo_b}) = **{punti_gruppo} punti**")
            else:
                st.write(f"- **{nome_gruppo}** ({len(carte)} carte): **{punti_gruppo} punti**")
                
            totale_generale += punti_gruppo
            
        st.markdown(f"--- \n ## 🏆 Punteggio Totale: **{totale_generale} punti**")

    # Eseguiamo il calcolo
    calcola_tutto()
