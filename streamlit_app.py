import streamlit

def authenticate(username, password):
    cursor.execute('SELECT username, password, role FROM dbo.Login WHERE username = ? AND password = ?',
    (username, password))
    user = cursor.fetchone()
    if user:
        return user[2]  # Return the role of the user
    return None

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1730204037185-b47267587b5e?q=80&w=1825&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-position: center;    
    background-repeat: no-repeat;
}   
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

def read_onlyoperator(read_only=False):
    if read_only:
        container_operator = st.container(height=None,border=True,key=None)
        container_operator.subheader('این قسمت توسط اپراتور انجام شده است')
        container_operator.text_input('شماره درخواست',key='tech_code',disabled=True)
        container_operator.selectbox('نام واحد',options=['Chipper',
                                                        'Conveyor Line',
                                                        'Energy Plant',
                                                        'Dryer & Air Grader',
                                                        'Refiner',
                                                        'Before Press',
                                                        'Press',
                                                        'After Press',
                                                        'Sanding & RBS',
                                                        'Cooling System'
                                                        'Steam Boiler',
                                                        'General'
                                                        ],key='section_name',disabled=True)
        container_operator.text_input('مشخصات دستگاه',key='machine_name',disabled=True)
        container_operator.selectbox('شیفت',options=[
                                                'A',
                                                'B',
                                                'C'
                                                ],key='shift',disabled=True)
        container_operator.text_input('نام درخواست کننده',key='operator',disabled=True)
        container_operator.selectbox('نوع عیب',options=[
                                                        'مکانیکی',
                                                        'برقی',
                                                        'تولید',
                                                        'تاسیسات',
                                                        'فلزکاری',
                                                        ], disabled=True)
        container_operator.subheader('تعیین زمان بروز اشکال')
        container_operator.selectbox('وضعیت توقف',options=['ندارد','دارد'],disabled=True)
        container_operator.date_input('زمان شروع توقف',key='stop',format="YYYY/MM/DD",disabled=True)
        container_operator.date_input('زمان پایان توقف',key='start',disabled=True)
    else:
        st.title('Operator Page')

# Define the pages
def admin_page():
    st.title('Admin Page')
    st.write('This is the admin page.')
    if st.button('Logout',key='logout_btn_admin'):
        st.session_state.role = None
        st.rerun()

def operator_page():
    st.title('Operator Page')
    container_operator = st.container(height=None,border=True,key=None)

    container_operator.subheader('این قسمت توسط اپراتور انجام می شود')
    container_operator.text_input('شماره درخواست',key='operator_code')
    container_operator.selectbox('نام واحد',options=['Chipper',
                                                    'Conveyor Line',
                                                    'Energy Plant',
                                                    'Dryer & Air Grader',
                                                    'Refiner',
                                                    'Before Press',
                                                    'Press',
                                                    'After Press',
                                                    'Sanding & RBS',
                                                    'Cooling System'
                                                    'Steam Boiler',
                                                    'General'
                                                    ],key='section_name')
    container_operator.text_input('مشخصات دستگاه',key='machine_name')
    container_operator.selectbox('شیفت',options=[
                                                'A',
                                                'B',
                                                'C'
                                                ],key='shift')
    container_operator.text_input('نام درخواست کننده',key='operator')
    container_operator.selectbox('نوع عیب',options=[
                                                    'مکانیکی',
                                                    'برقی',
                                                    'تولید',
                                                    'تاسیسات',
                                                    'فلزکاری'
                                                    ])
    container_operator.subheader('تعیین زمان بروز اشکال')
    container_operator.selectbox('وضعیت توقف',options=['ندارد','دارد'])
    container_operator.date_input('زمان شروع توقف',key='stop',format="YYYY/MM/DD")
    container_operator.date_input('زمان پایان توقف',key='start')

    if container_operator.button('ثبت',key='operator_section'):
        st.success('Everything Works Fine')
    if st.button('Logout',key='logout_btn_operator'):
        st.session_state.role = None
        st.rerun()

def technician_page():
    st.title('Technician Page')
    read_onlyoperator(read_only=True)
    @st.dialog('اقلام')
    def show_aghlam_form():
        aghlam_form()

    def aghlam_form():
        with st.form('aghlam_form'):
            form_code = st.text_input('کد درخواست')
            form_date = st.date_input('تاریخ')
            form_discription = st.text_input('شرح قلم')
            form_numb = st.text_input('تعداد قلم')
            form_unit = st.selectbox('نوع قلم', options=['عدد','متر','سانتی متر','میلی متر','گرم','کیلوگرم','لیتر'])
            submit_button = st.form_submit_button('ثبت اقلام')   
            
             
            if submit_button:
                st.success('Congratulations')
                
    container_technisian = st.container(height=None,border=True,key=None)

    container_technisian.subheader('این قسمت توسط واحد انجام دهنده تعمیرات تکمیل می گردد')
    container_technisian.selectbox('نوع تعمیرات',options=['EM','CM','GM','PM'],key='problem_type')
    container_technisian.selectbox('نوع خدمات',options=['بازرسی و چک','تنظیم','آچارکشی','روانکاری','تعمیر','تعویض'],key='service_type')
    container_technisian.selectbox('علت خرابی',options=['استهلاک طبیعی','عدم دقت اپراتور','نامناسب بودن تعمیرات قبلی','کیفیت پایین قطعه یدکی','سرویس و نگهداری نامناسب'],key='failure_type')
    container_technisian.subheader('زمان های انجام کار')
    container_technisian.time_input('مدت تشخیص عیب',key='problem_time')
    container_technisian.time_input('مدت تهیه لوازم یدکی',key='aghlam_time')
    container_technisian.time_input('مدت انجام عملیات',key='operation_time')
    container_technisian.time_input('مدت راه اندازی خط',key='start_time')
    container_technisian.time_input('زمان تلف شده',key='wasted_time')
    container_technisian.time_input('جمع کل زمان عملیات',key='total_time')
    container_technisian.text_input('نفر ساعت صرف شده',key='person_time')
    container_technisian.text_area(':علت تاخیرات',key='discription')
    container_technisian.text_area(':شرح کامل اقدامات انجام شده جهت رفع عیب',key='problem')

    if container_technisian.button('ثبت',key='Submit'):
        st.success('Everything is fine')
        
    if container_technisian.button('اقلام',key=''):
        show_aghlam_form()
    if st.button('Logout',key='logout_btn_technician'):
        st.session_state.role = None
        st.rerun()



# Initialize session state
if 'role' not in st.session_state:
    st.session_state.role = None

# Streamlit app
if st.session_state.role is None:
    st.title('Login Page')
    # Login form
 
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    login_button = st.button('Login',key='login_btn')

    if login_button:
        role = authenticate(username, password)
        if role:
            st.success(f'Welcome {username}!')
            st.session_state.role = role
            st.rerun()
        else:
            st.error('Invalid username or password')
else:
    if st.session_state.role == 'admin':
        admin_page()
    elif st.session_state.role == 'operator':
        operator_page()
    elif st.session_state.role == 'technician':
        technician_page()
