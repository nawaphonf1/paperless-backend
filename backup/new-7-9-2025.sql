PGDMP  :    5    
    	        }         	   paperless    17.5    17.5 C    9           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            :           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            ;           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            <           1262    16460 	   paperless    DATABASE     �   CREATE DATABASE paperless WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE paperless;
                     postgres    false            �            1259    16461    categories_id_seq    SEQUENCE     z   CREATE SEQUENCE public.categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public               postgres    false            �            1259    16486 
   categories    TABLE     �   CREATE TABLE public.categories (
    categories_id integer DEFAULT nextval('public.categories_id_seq'::regclass) NOT NULL,
    categories_name character varying(100) NOT NULL,
    categories_desc character varying(100)
);
    DROP TABLE public.categories;
       public         heap r       postgres    false    217            �            1259    16462    dept_dept_id_seq    SEQUENCE     y   CREATE SEQUENCE public.dept_dept_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.dept_dept_id_seq;
       public               postgres    false            �            1259    16492    dept    TABLE     �   CREATE TABLE public.dept (
    dept_id integer DEFAULT nextval('public.dept_dept_id_seq'::regclass) NOT NULL,
    dept_name character varying(100) NOT NULL,
    dept_name_short character varying(100) NOT NULL
);
    DROP TABLE public.dept;
       public         heap r       postgres    false    218            �            1259    16466 
   doc_id_seq    SEQUENCE     s   CREATE SEQUENCE public.doc_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 !   DROP SEQUENCE public.doc_id_seq;
       public               postgres    false            �            1259    16527    doc    TABLE     (  CREATE TABLE public.doc (
    doc_id integer DEFAULT nextval('public.doc_id_seq'::regclass) NOT NULL,
    doc_name character varying(100) NOT NULL,
    doc_no character varying(100) NOT NULL,
    categories_id integer NOT NULL,
    doc_desc character varying(100) NOT NULL,
    critical_level integer NOT NULL,
    doc_type character varying(20) NOT NULL,
    created_by text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_by text NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);
    DROP TABLE public.doc;
       public         heap r       postgres    false    222            �            1259    16463    doc_history_id_seq    SEQUENCE     {   CREATE SEQUENCE public.doc_history_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.doc_history_id_seq;
       public               postgres    false            �            1259    16498    doc_history    TABLE     �  CREATE TABLE public.doc_history (
    doc_history_id integer DEFAULT nextval('public.doc_history_id_seq'::regclass) NOT NULL,
    doc_id integer NOT NULL,
    action character varying(50) NOT NULL,
    action_by character varying(50) NOT NULL,
    action_detail text,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    created_by character varying(50) NOT NULL
);
    DROP TABLE public.doc_history;
       public         heap r       postgres    false    219            �            1259    16464    doc_path_id_seq    SEQUENCE     x   CREATE SEQUENCE public.doc_path_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.doc_path_id_seq;
       public               postgres    false            �            1259    16507    doc_path    TABLE     3  CREATE TABLE public.doc_path (
    doc_path_id integer DEFAULT nextval('public.doc_path_id_seq'::regclass) NOT NULL,
    doc_id integer NOT NULL,
    path character varying(100) NOT NULL,
    created_by text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    file_name text
);
    DROP TABLE public.doc_path;
       public         heap r       postgres    false    220            �            1259    16465    doc_recipter_id_seq    SEQUENCE     |   CREATE SEQUENCE public.doc_recipter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.doc_recipter_id_seq;
       public               postgres    false            �            1259    16516    doc_recipter    TABLE     �  CREATE TABLE public.doc_recipter (
    doc_recipter_id integer DEFAULT nextval('public.doc_recipter_id_seq'::regclass) NOT NULL,
    doc_id integer NOT NULL,
    units_id integer NOT NULL,
    is_read boolean DEFAULT false NOT NULL,
    recip_status character varying(20) DEFAULT 'รอดำเนินการ'::character varying NOT NULL,
    created_by text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    recipter_desc text
);
     DROP TABLE public.doc_recipter;
       public         heap r       postgres    false    221            �            1259    32817    doc_sign_id_seq    SEQUENCE     x   CREATE SEQUENCE public.doc_sign_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.doc_sign_id_seq;
       public               postgres    false            �            1259    32807    doc_sign    TABLE     T  CREATE TABLE public.doc_sign (
    doc_sign_id integer DEFAULT nextval('public.doc_sign_id_seq'::regclass) NOT NULL,
    doc_id integer NOT NULL,
    units_id integer NOT NULL,
    path text NOT NULL,
    sign_desc text,
    created_by text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    file_name text
);
    DROP TABLE public.doc_sign;
       public         heap r       postgres    false    240            �            1259    16467    page_id_seq    SEQUENCE     t   CREATE SEQUENCE public.page_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.page_id_seq;
       public               postgres    false            �            1259    16537    page    TABLE     �   CREATE TABLE public.page (
    page_id integer DEFAULT nextval('public.page_id_seq'::regclass) NOT NULL,
    page_no integer NOT NULL,
    page_name character varying(100) NOT NULL
);
    DROP TABLE public.page;
       public         heap r       postgres    false    223            �            1259    16468    permission_id_seq    SEQUENCE     z   CREATE SEQUENCE public.permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.permission_id_seq;
       public               postgres    false            �            1259    16543 
   permission    TABLE       CREATE TABLE public.permission (
    permission_id integer DEFAULT nextval('public.permission_id_seq'::regclass) NOT NULL,
    units_id integer NOT NULL,
    page_id integer NOT NULL,
    created_at time without time zone DEFAULT now() NOT NULL,
    created_by text NOT NULL
);
    DROP TABLE public.permission;
       public         heap r       postgres    false    224            �            1259    16469    position_position_id_seq    SEQUENCE     �   CREATE SEQUENCE public.position_position_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.position_position_id_seq;
       public               postgres    false            �            1259    16552    position    TABLE       CREATE TABLE public."position" (
    position_id integer DEFAULT nextval('public.position_position_id_seq'::regclass) NOT NULL,
    position_name character varying(100) NOT NULL,
    position_name_short character varying(100) NOT NULL,
    position_seq integer NOT NULL
);
    DROP TABLE public."position";
       public         heap r       postgres    false    225            �            1259    24579    units_id_seq    SEQUENCE     u   CREATE SEQUENCE public.units_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.units_id_seq;
       public               postgres    false            �            1259    16558    units    TABLE     W  CREATE TABLE public.units (
    units_id integer DEFAULT nextval('public.units_id_seq'::regclass) NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL,
    position_id integer NOT NULL,
    dept_id integer,
    post_code bigint,
    address_detail text,
    identify_id text,
    status text,
    is_active boolean DEFAULT true NOT NULL,
    img_path text,
    identify_soldier_id text,
    tel text,
    blood_group text,
    position_detail text,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    created_by text NOT NULL
);
    DROP TABLE public.units;
       public         heap r       postgres    false    238            �            1259    16471    users    TABLE     �  CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(100) NOT NULL,
    hashed_password text NOT NULL,
    is_active boolean DEFAULT false,
    role character varying(50) DEFAULT 'user'::character varying,
    units_id integer DEFAULT 0,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    created_by text DEFAULT 'anonimaser'::text NOT NULL
);
    DROP TABLE public.users;
       public         heap r       postgres    false            �            1259    16470    users_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_user_id_seq;
       public               postgres    false    227            =           0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
          public               postgres    false    226            X           2604    16474    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public               postgres    false    226    227    227            *          0    16486 
   categories 
   TABLE DATA           U   COPY public.categories (categories_id, categories_name, categories_desc) FROM stdin;
    public               postgres    false    228   �R       +          0    16492    dept 
   TABLE DATA           C   COPY public.dept (dept_id, dept_name, dept_name_short) FROM stdin;
    public               postgres    false    229   �R       /          0    16527    doc 
   TABLE DATA           �   COPY public.doc (doc_id, doc_name, doc_no, categories_id, doc_desc, critical_level, doc_type, created_by, created_at, updated_by, updated_at) FROM stdin;
    public               postgres    false    233   �S       ,          0    16498    doc_history 
   TABLE DATA           w   COPY public.doc_history (doc_history_id, doc_id, action, action_by, action_detail, created_at, created_by) FROM stdin;
    public               postgres    false    230   �T       -          0    16507    doc_path 
   TABLE DATA           `   COPY public.doc_path (doc_path_id, doc_id, path, created_by, created_at, file_name) FROM stdin;
    public               postgres    false    231   �V       .          0    16516    doc_recipter 
   TABLE DATA           �   COPY public.doc_recipter (doc_recipter_id, doc_id, units_id, is_read, recip_status, created_by, created_at, recipter_desc) FROM stdin;
    public               postgres    false    232   GX       5          0    32807    doc_sign 
   TABLE DATA           u   COPY public.doc_sign (doc_sign_id, doc_id, units_id, path, sign_desc, created_by, created_at, file_name) FROM stdin;
    public               postgres    false    239   �Y       0          0    16537    page 
   TABLE DATA           ;   COPY public.page (page_id, page_no, page_name) FROM stdin;
    public               postgres    false    234   b\       1          0    16543 
   permission 
   TABLE DATA           ^   COPY public.permission (permission_id, units_id, page_id, created_at, created_by) FROM stdin;
    public               postgres    false    235   �\       2          0    16552    position 
   TABLE DATA           c   COPY public."position" (position_id, position_name, position_name_short, position_seq) FROM stdin;
    public               postgres    false    236   o]       3          0    16558    units 
   TABLE DATA           �   COPY public.units (units_id, first_name, last_name, position_id, dept_id, post_code, address_detail, identify_id, status, is_active, img_path, identify_soldier_id, tel, blood_group, position_detail, created_at, created_by) FROM stdin;
    public               postgres    false    237   I^       )          0    16471    users 
   TABLE DATA           v   COPY public.users (user_id, username, hashed_password, is_active, role, units_id, created_at, created_by) FROM stdin;
    public               postgres    false    227   _       >           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 3, true);
          public               postgres    false    217            ?           0    0    dept_dept_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.dept_dept_id_seq', 1, false);
          public               postgres    false    218            @           0    0    doc_history_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.doc_history_id_seq', 17, true);
          public               postgres    false    219            A           0    0 
   doc_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('public.doc_id_seq', 8, true);
          public               postgres    false    222            B           0    0    doc_path_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.doc_path_id_seq', 9, true);
          public               postgres    false    220            C           0    0    doc_recipter_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.doc_recipter_id_seq', 21, true);
          public               postgres    false    221            D           0    0    doc_sign_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.doc_sign_id_seq', 32, true);
          public               postgres    false    240            E           0    0    page_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.page_id_seq', 6, true);
          public               postgres    false    223            F           0    0    permission_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.permission_id_seq', 13, true);
          public               postgres    false    224            G           0    0    position_position_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.position_position_id_seq', 1, false);
          public               postgres    false    225            H           0    0    units_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.units_id_seq', 2, true);
          public               postgres    false    238            I           0    0    users_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_user_id_seq', 2, true);
          public               postgres    false    226            y           2606    16491    categories categories_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (categories_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public                 postgres    false    228            {           2606    16497    dept dept_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.dept
    ADD CONSTRAINT dept_pkey PRIMARY KEY (dept_id);
 8   ALTER TABLE ONLY public.dept DROP CONSTRAINT dept_pkey;
       public                 postgres    false    229            }           2606    16506    doc_history doc_history_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.doc_history
    ADD CONSTRAINT doc_history_pkey PRIMARY KEY (doc_history_id);
 F   ALTER TABLE ONLY public.doc_history DROP CONSTRAINT doc_history_pkey;
       public                 postgres    false    230                       2606    16515    doc_path doc_path_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.doc_path
    ADD CONSTRAINT doc_path_pkey PRIMARY KEY (doc_path_id);
 @   ALTER TABLE ONLY public.doc_path DROP CONSTRAINT doc_path_pkey;
       public                 postgres    false    231            �           2606    16536    doc doc_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.doc
    ADD CONSTRAINT doc_pkey PRIMARY KEY (doc_id);
 6   ALTER TABLE ONLY public.doc DROP CONSTRAINT doc_pkey;
       public                 postgres    false    233            �           2606    16526    doc_recipter doc_recipter_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.doc_recipter
    ADD CONSTRAINT doc_recipter_pkey PRIMARY KEY (doc_recipter_id);
 H   ALTER TABLE ONLY public.doc_recipter DROP CONSTRAINT doc_recipter_pkey;
       public                 postgres    false    232            �           2606    32811    doc_sign doc_sign_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.doc_sign
    ADD CONSTRAINT doc_sign_pkey PRIMARY KEY (doc_sign_id);
 @   ALTER TABLE ONLY public.doc_sign DROP CONSTRAINT doc_sign_pkey;
       public                 postgres    false    239            �           2606    16542    page page_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.page
    ADD CONSTRAINT page_pkey PRIMARY KEY (page_id);
 8   ALTER TABLE ONLY public.page DROP CONSTRAINT page_pkey;
       public                 postgres    false    234            �           2606    16551    permission permission_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.permission
    ADD CONSTRAINT permission_pkey PRIMARY KEY (permission_id);
 D   ALTER TABLE ONLY public.permission DROP CONSTRAINT permission_pkey;
       public                 postgres    false    235            �           2606    16557    position position_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (position_id);
 B   ALTER TABLE ONLY public."position" DROP CONSTRAINT position_pkey;
       public                 postgres    false    236            �           2606    16566    units units_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.units
    ADD CONSTRAINT units_pkey PRIMARY KEY (units_id);
 :   ALTER TABLE ONLY public.units DROP CONSTRAINT units_pkey;
       public                 postgres    false    237            u           2606    16483    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    227            w           2606    16485    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public                 postgres    false    227            *   4   x�3�|�c������`gÃ�F[��0���2Ƨ��"F��� �X*�      +   �   x���M
�0�יSx�BR.�a,�^@���v!.,/�yG1L5��.
�0�y�ތ5DA܉=�15o5�ĕ qf�^+'��pXX3�gV�$7%9Y�%�SR.�_�Q94����)-
߷��ln�����lCI4���~�ō��j���<�梭��,d����aa      /   .  x����J1���S�l��d&?����Jcۃ=���Ļ xԛ"^���QLw���0����&��(��䇒_K~/���oK~SH�/���z�Q�g=�����]�/��~��Ű��lj�����S�L��D1��h~��~�Lu�q�ƶ�z�=ڮ6�.��|�F�a��+�Viܭ�CڥݩF��h�"G�s�v��̼�(�L�:��~���IW�02�H��#5��gI��A+�1�dE���9�D��(t���hQ9�C��~z���j��s��F�*�ߤ�M�K%����4b      ,   �  x����N1@k�Wl�*�g<���Z�����>�K*T!q������|
��]PġEr�{��͌A����q��	��G\�r|⸗�)2����������g9�v.{�@��W�V	�r���A5�ZT�WO9��w�[d�~��9%��0�K�W��d}��q�]�*��C������.UwF�;z*h�����d�\�$�Fr0���qc�����c���,���7��珗  �"Tm����~4XV��M�WA{YY@�2f�_��/�m	:�����m����?o����$�5C$̿q]Z���䛆����%��&� J�A���Z�~J��[,{����<ؗ���@(+c�����:Oʼ���_�D鍧�e�c�,��x=J��      -   �  x��S�n1��O�2)�̌�AC�R�w�"A�t�'	ҥHE�DA(⼍��S�8����۳��x��G���ê�r���<�ۜ~�tU>��'�o9��Ӝ��t��'2����w\�����������C��h�	�ȵFt�4���c��vnFF2>���
��ӅC=q��˱�w2ԉ��ZI�9�Yi~�����g>}_l�U˧�������T]�kpr]���W��F��{Uq?��ѫ���*���	E�a���Iyٍ��ѻO�8	!�5)�@���.o��C,���F"���NXQ�?�=^��=���.x��q<�D���A���Hk(aX -q؈B�u\� ��W�r),'��Z���
Zڊ-x�����O��i�Ώ������B�!���ө�i��0;Q      .   z  x���;N�0��9E.�֌=�}N�B����	h(x��!Q�(�m|Ǝ+`��HQ��4��A��ͥ�屖�Z���U-O�����Z���k-;s|r~va8� �5"e�Lbŧ�l�o�	�T�]�����N�7�ݯj���q4*�=Yf�0V��b�E�T�+� |oTTõ��4Rmڃj/�<�7��=F��I���s� �d{
CPm���5�zm��-Z�>�Թ��E��,��@������~Y��.��xIYaD�1e�,y���e��s�W��)3[I�FYӱTZYF����ZF���}{iDȀ���)F���f����<y?yQ�>��!u��ԛ������,��@�>�	��C׌�H�'�{Z�v�O�F��      5   �  x�Օ�n�0��٧�#�zf���Cp��*��+��;�/��8�J �B�6y&^Z��9n�Dvb�7�{>�UP�l�mW��~���j�q8S�p����}>���qx;����8���o��^�����ջ�u�w��J�l.��K��s����C���r7�2��4��z���VO�:��l+�h�4!/AGQ[L@K2gP�����A(X>��e%Er�4�|�Jl$1(�H��C��^��E 	.0�S�?J�'!ǰ���zw5��=�v/8��+)�ڲ�H[D&�X���:��HP�c�At ��k>�-�O��R��&
D���h|���gK��n.=�F�І=t?�2�H��&�t?�nm�w�H�Zy>�Ls隚Đl�.тʈW9=�tH�h�E�T9DعL�����î������w.Hd:������&�&���[r9f���]�[n�짛h0��ݕ��]���ߦCˀ��t:�]����_|�/�jAy`m|u7캈,��3�v��A.v��������ڦ��l��nl-�X�CS�)����C���i	�Cc�1��80^�hu �?�#}�����%����c9"�O�p�a��=T�J�r_M�"��+$�R�E�J-����GJ      0   �   x�}�;�`�g�. �y��@aF�Zu��@0�����4�X"���8C�?�M<�_�.�bR�(���"x���9��
����^g%ʭ/� �c}��U�|���v�����kԈ�~w�-�c��l�f6�4�c      1   j   x�u�=�0�9=L�8�y�YX�X��#)z#V�O��*&U�L�S5�f�!�q�w2y��b��JX!���_���:���p�k	1�@0\?8Õ+=��rJ�QG}      2   �   x�}�M�0�ם��a(�w�0�
`�.��5a��d���B)C\>��}o�����2]��L����VI�~wd�G��"�{���0��
+*�*��*��)�t-�>i�)d�ə��vC��q�ipoS�qe%�?�\c\F������t	�����gh��0��G�T��~nygz,n��5[�C��$�i��v ���#e      3   �   x�eN]
�0{nO�l�u��vO�K�͹�j���C<��{�ӣ�(�!��p�)�c������@)�h1�=x$d<�G�SwL@d,�#�IΑ�[W��*ں{1���36�T띫F��iƶ.�q�!v0*W�$����[U�t��M�5C��5:t��w�B"Ic�����QI��L$����1�mY      )   �   x�U�AO�0 �s������o�m��"�;�$^�����1I�^4z���@�4E�4q
�|y*s���xXn�K��v~�n$�9c:zzߧP4׭��63va���2����� .��d��~�[[�@��`�ҹʎ�i_5���~,���M|���>�S��k��q=�>�I}9������DS�� �����gDa     