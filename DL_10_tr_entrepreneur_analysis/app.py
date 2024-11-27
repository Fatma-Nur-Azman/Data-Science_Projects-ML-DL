import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Giriş Sayfası: Başlık ve görsellerle birlikte bilgilendirme
def home_page():
    # Türkiye Yapay Zeka İnisiyatifi Bilgisi
    # Sütun yapısını oluştur
    col1, col2 = st.columns([6,1])  # Sol taraf 1 birim, sağ taraf 3 birim genişliğinde

    # Sol tarafa logo ekle
    with col1:
        st.markdown(
            """
            <div style="background-color:#726c80;padding:14px;border-radius:10px;">
                <h2 style="text-align:center;color:white;">Türkiye Yapay Zeka Girişimleri Analiz Platformu'na Hoş Geldiniz!</h2>
                <p style="color:white;font-size:16px;text-align:center;">
                    Türkiye'deki yapay zeka girişimlerini tanımanız, analiz etmeniz ve bu girişimlerden ilham almanız için tasarlandı. İş arayanlar için doğru firmayı bulmayı, sektörle ilgili yenilikleri keşfetmek isteyenlere rehber olmayı ve yapay zeka dünyasına ilgi duyan herkes için bir bilgi merkezi olmayı hedefliyorum. 
                    
              
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Sağ tarafa başlık ve metni ekle
    with col2:
        st.image("https://fatmanurazman.vercel.app/images/icon1.png", width=100)
    

    # Ekstra bilgilendirme alt kısmında
    st.markdown(
        """
        <div style="background-color:#f0f0f0b0;padding:15px;border-radius:10px;">
            <p style="text-align:justify;font-size:16px;">
            <strong>Platformumda neler bulabilirsiniz?</strong> <br><br>
            <strong>Kategorilere Göre Girişimci Analizi</strong> :  sekmesinde, girişimleri alanlarına göre keşfedin. Grafikler ve istatistiklerle hangi alanın ne kadar popüler olduğunu görün.<br>
            <strong>Girişimcilerin Bilgileri</strong> : sekmesinde, ilginizi çeken girişimlerin detaylarını öğrenin ve dilerseniz web sitelerine yönlendirilin.<br>
            Bu projeyi hayata geçirme sürecinde, Türkiye Yapay Zeka İnisiyatifi'nin (turkiye.ai) sunduğu verilere dayandım. Amacım, herkes için yapay zeka ekosistemine dair değerli bir kaynak yaratmak.<br><br>
            Sorularınız ya da geri bildirimleriniz için bana LinkedIn üzerinden ulaşabilirsiniz.<br>
            Umarım platformumdan keyif alır ve yararlı bulursunuz! 😊<br><br>
            <strong>Hazırlayan:</strong> Fatma Nur Azman<br>
            <a href="https://www.linkedin.com/in/fatmanurazman/" style="color:#00aced;text-decoration:none;" target="_blank">LinkedIn: Fatma Nur Azman</a><br><br>
            Veri Çekme Tarihi: 25.11.2024
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Mor görsel
    st.image("https://turkiye.ai/wp-content/uploads/2020/06/slider-image-2.jpg", use_column_width=True)

# Veri Görselleştirme Sayfası

def visualization_page(data):
    # Veri Görselleştirme Başlığı
    st.title("Kategorilere Göre Girişimci Analizi")
    
    # Kullanıcıdan gösterilecek kategori sayısını al
    max_categories = st.slider(
        "Gösterilecek Kategori Sayısı", 
        min_value=5, 
        max_value=50, 
        value=20,
        step=5,
        help="Grafikte gösterilecek kategori sayısını seçin"
    )
    
    # Categories sütunundaki listeleri düzleştir
    category_counts = {}
    
    # Her bir kategoriyi say
    for categories in data['Categories']:
        if isinstance(categories, str):
            categories = categories.strip('[]').split(',')
        
        for category in categories:
            clean_category = (category.strip()
                            .strip("'")
                            .strip('"')
                            .strip('[]')
                            .replace("'", "")
                            .replace('"', "")
                            .strip())
            
            if clean_category:
                category_counts[clean_category] = category_counts.get(clean_category, 0) + 1
    
    # Dictionary'i Series'e çevir ve sırala
    category_series = pd.Series(category_counts).sort_values(ascending=False)
    category_series = category_series.head(max_categories)

    if len(category_series) == 0:
        st.write("Hiçbir kategori bulunamadı!")
        return

    # Yeni figür oluştur
    plt.style.use('default')  # Varsayılan stili kullan
    fig, ax = plt.subplots(figsize=(12, max_categories/2))
    
    # Renk paleti
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(category_series)))
    
    # Bar plot
    bars = sns.barplot(
        x=category_series.values, 
        y=category_series.index, 
        ax=ax,
        palette=colors
    )
    
    # Bar değerlerini ekle
    for i, v in enumerate(category_series.values):
        ax.text(v, i, f' {v}', va='center')

    # Başlık ve etiketler
    ax.set_title("Kategori Bazında Şirket Dağılımı", size=20, pad=20)
    ax.set_xlabel("Şirket Sayısı", size=20, labelpad=10)
    
    # Izgara
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)
    
    # Font boyutlarını ayarla
    ax.tick_params(axis='both', which='major', labelsize=12)
    
    # Düzen
    plt.tight_layout()
    
    # Grafiği göster
    st.pyplot(fig)

    # Kategori istatistikleri
    st.write("### Kategori İstatistikleri")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Toplam Kategori Sayısı", len(category_counts))
    with col2:
        st.metric("En Yüksek Şirket Sayısı", category_series.max())
    with col3:
        st.metric("Ortalama Şirket Sayısı", round(category_series.mean(), 1))
    
    # Kategori Arama Bölümü
    st.write("### Kategoriye Özel Şirket Bilgileri Arama")
    search_term = st.text_input("Kategori Ara Örn:Optimizasyon", "")
    if search_term:
        # Kategorilerde arama yap
        mask = data['Categories'].apply(lambda x: 
            search_term.lower() in str(x).lower()
        )
        search_results = data[mask]
        
        if not search_results.empty:
            st.write(f"**{len(search_results)} şirket bulundu.**")
            
            # Her bir sonuç için özel format
            for _, row in search_results.iterrows():
                col1, col2, col3 = st.columns([3, 2, 2])
                
                with col1:
                    st.write(f"**{row['Title']}**")
                
                with col2:
                    st.write(f"Kurucu: {row['Founder']}")
                
                with col3:
                    # URL'yi tıklanabilir link olarak göster
                    st.markdown(f"[Web Sitesi]({row['Site URL']})")
                
                # İnce çizgi ekle
                st.markdown("---")
        else:
            st.warning(f"'{search_term}' kategorisinde şirket bulunamadı.")
  


# Ana Uygulama
def app():
    st.sidebar.title("Sayfa Seçimi")
    page = st.sidebar.radio("Sayfalar", ["Giriş Sayfası", "Kategorilere Göre Girişimci Analizi", "Girişimcilerin Bilgileri"])

    # CSV dosyasını oku
    data = pd.read_csv("girisimci_data.csv")

    # "Categories" sütunundaki değerleri listeye çevir
    data['Categories'] = data['Categories'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])

    if page == "Giriş Sayfası":
        home_page()

    elif page == "Kategorilere Göre Girişimci Analizi":
        visualization_page(data)

    elif page == "Girişimcilerin Bilgileri":
        st.title("Girişimlerin Filtrelenmesi")

        # Kategorileri temizle ve unique hale getir
        def clean_category(cat):
            if isinstance(cat, str):
                return cat.strip("[]'\" ").replace("'", "").replace('"', "").strip()
            return cat

        # Tüm kategorileri düzleştir ve benzersiz hale getir
        all_categories = []
        for cats in data['Categories']:
            if isinstance(cats, str):
                # String'i liste haline getir ve temizle
                categories = [clean_category(c) for c in eval(cats)]
            else:
                # Zaten liste ise direkt temizle
                categories = [clean_category(c) for c in cats]
            all_categories.extend(categories)
        
        # Benzersiz kategoriler
        unique_categories = sorted(set(all_categories))

        # Arama kutusu ve filtreleme
        st.sidebar.write("### Kategori Filtreleme")
        search_term = st.sidebar.text_input(
            "Kategori Ara örn:Görüntü İşleme",
            help="Kategori adını yazın veya benzer kategorilerden seçin"
        )

        # Benzer kategorileri bul
        if search_term:
            similar_categories = [
                cat for cat in unique_categories 
                if search_term.lower() in cat.lower()
            ]
            
            if similar_categories:
                selected_category = st.sidebar.selectbox(
                    "Benzer Kategoriler:",
                    options=["Tümü"] + similar_categories,
                    help="Bulunan benzer kategorilerden seçim yapın"
                )
            else:
                st.sidebar.warning("Eşleşen kategori bulunamadı.")
                selected_category = "Tümü"
        else:
            selected_category = "Tümü"

        # Filtreleme işlemi
        if selected_category == "Tümü":
            filtered_data = data
        else:
            filtered_data = data[data['Categories'].apply(
                lambda x: selected_category in (
                    [clean_category(c) for c in (x if isinstance(x, list) else eval(x))]
                )
            )]

        # Filtrelenmiş sonuçları göster
        st.write(f"### Filtrelenmiş Girişimler ({len(filtered_data)} sonuç)")
        
        # Her girişim için kart benzeri görünüm
        for index, row in filtered_data.iterrows():
            with st.container():
                col1, col2, col3 = st.columns([3, 2, 2])
                
                with col1:
                    st.write(f"**{row['Title']}**")
                
                with col2:
                    st.write(f"Kurucu: {row['Founder']}")
                
                with col3:
                    st.markdown(f"[🔗 Web Sitesi]({row['Site URL']})")
                
                # Kategorileri temiz şekilde göster
                categories = row['Categories']
                if isinstance(categories, str):
                    categories = [clean_category(c) for c in eval(categories)]
                else:
                    categories = [clean_category(c) for c in categories]
                st.write("Kategoriler:", ", ".join(categories))
                
                st.markdown("---")

        # Detaylı girişim inceleme
        if not filtered_data.empty:
            st.write("### Girişim Detayları")
            
            selected_company = st.selectbox(
                "Detaylarını görmek istediğiniz girişimi seçin:",
                options=filtered_data['Title'].tolist(),
                help="Bir girişim seçerek detaylı bilgileri görüntüleyebilirsiniz"
            )

            if selected_company:
                company_details = filtered_data[filtered_data['Title'] == selected_company].iloc[0]
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.write("#### Genel Bilgiler")
                    st.write(f"**Şirket Adı:** {company_details['Title']}")
                    st.write(f"**Kurucu:** {company_details['Founder']}")
                    
                with col2:
                    st.write("#### Bağlantılar")
                    st.markdown(f"**[🌐 Web Sitesini Ziyaret Et]({company_details['Site URL']})**")
                
                st.write("#### Kategoriler")
                categories = company_details['Categories']
                if isinstance(categories, str):
                    categories = [clean_category(c) for c in eval(categories)]
                else:
                    categories = [clean_category(c) for c in categories]
                
                category_html = " ".join([
                    f'<span style="background-color: #f0f2f6; padding: 4px 12px; '
                    f'border-radius: 16px; margin: 4px; display: inline-block;">{cat}</span>'
                    for cat in categories
                ])
                st.markdown(f'<div style="margin: 10px 0;">{category_html}</div>', unsafe_allow_html=True)
    
  

if __name__ == "__main__":
    app()
