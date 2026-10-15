import pandas as pd
import streamlit as st

st.set_page_config(page_title="دليل كندا - عم هاني", page_icon="🍁", layout="wide")

st.title("🍁 دليل كندا الشامل - كابتن هاني")
st.caption("التطبيق ده متصمم مخصوص عشان تظبط تكتيك السفرية وتوفر المصاريف!")

tab1, tab2, tab3, tab4 = st.tabs(["📍 خط الرحلة", "✅ تجهيزات الماتش", "💰 محفظة البطولة", "💡 تكتيكات التوفير"])

with tab1:
    st.header("📍 خط الرحلة")
    st.subheader("30 October 2026")

    st.markdown(
        """
        - Halifax: 8 days — Cold/Rainy — Wear waterproof jacket.
        - Visit Halifax Waterfront, Citadel, Peggy's Cove, and Saint Mena's Coptic Orthodox Church.
        - Ottawa: 3 days (from Nov 7) — Very cold — Wear thermal layers.
        - Visit Parliament and St. Mary Coptic Church.
        - Toronto: 39 hours transit (from Nov 10) — Leave luggage in storage.
        - Visit CN Tower, Walmart, and Winners (to buy Panini cards for Karas and gifts for Chris).
        """
    )

with tab2:
    st.header("✅ تجهيزات الماتش")
    st.error("كارت أحمر: إياك تفتح بيانات التجوال للخط المصري عشان الرصيد ميتسحبش!")

    st.checkbox("Offline Google Maps Canada", value=False)
    st.checkbox("Transit app for offline bus schedules", value=False)
    st.checkbox("XE Currency", value=False)
    st.checkbox("WiFi Map / Instabridge for free wifi hotspots", value=False)
    st.checkbox("Offline Google Translate", value=False)
    st.checkbox("Save passport/visa as PDFs", value=False)

with tab3:
    st.header("💰 محفظة البطولة")

    if "expenses" not in st.session_state:
        st.session_state.expenses = []

    with st.form("expenses_form"):
        item = st.text_input("اشتريت إيه؟")
        cost = st.number_input("بكام دولار كندي؟", min_value=0.0, step=1.0, format="%.2f")
        submitted = st.form_submit_button("إضافة المصروف")

        if submitted and item.strip():
            st.session_state.expenses.append({"الاسم": item.strip(), "المبلغ (CAD)": float(cost)})
            st.success("تمت إضافة المصروف بنجاح")

    if st.session_state.expenses:
        expenses_df = pd.DataFrame(st.session_state.expenses)
        st.table(expenses_df)
        total = float(expenses_df["المبلغ (CAD)"].sum())
        st.warning(f"إجمالي المصاريف: {total:.2f} دولار كندي")
    else:
        st.info("ما في مصاريف مسجلة لحد دلوقتي.")

    if st.button("مسح كل المصاريف"):
        st.session_state.expenses.clear()
        st.rerun()

with tab4:
    st.header("💡 تكتيكات التوفير")
    st.write("• Eat at Tim Hortons and Walmart.")
    st.write("• Avoid 15% tips in dine-in restaurants by getting fast food.")
    st.write("• Canadian visa does NOT allow entry to the US, for example Niagara Falls US side.")
    st.write("• Roll clothes in luggage to save space.")
    st.write("• Carry the heavy jacket on the plane to save weight.")

st.markdown(
    "<div style='text-align: center; margin-top: 2rem; font-size: 1.1rem;'>صُنع بحب وتكتيك عالي بواسطة كاراس 👨‍💻⚽</div>",
    unsafe_allow_html=True,
)
