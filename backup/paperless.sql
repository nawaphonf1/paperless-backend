PGDMP      ;                }         	   paperless    17.5    17.5 >    .           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            /           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            0           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            1           1262    16460 	   paperless    DATABASE     �   CREATE DATABASE paperless WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
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
       public               postgres    false            �            1259    16507    doc_path    TABLE       CREATE TABLE public.doc_path (
    doc_path_id integer DEFAULT nextval('public.doc_path_id_seq'::regclass) NOT NULL,
    doc_id integer NOT NULL,
    path character varying(100) NOT NULL,
    created_by text NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL
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
       public         heap r       postgres    false    221            �            1259    16467    page_id_seq    SEQUENCE     t   CREATE SEQUENCE public.page_id_seq
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
       public               postgres    false    227            2           0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
          public               postgres    false    226            S           2604    16474    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public               postgres    false    226    227    227            !          0    16486 
   categories 
   TABLE DATA           U   COPY public.categories (categories_id, categories_name, categories_desc) FROM stdin;
    public               postgres    false    228   JL       "          0    16492    dept 
   TABLE DATA           C   COPY public.dept (dept_id, dept_name, dept_name_short) FROM stdin;
    public               postgres    false    229   �L       &          0    16527    doc 
   TABLE DATA           �   COPY public.doc (doc_id, doc_name, doc_no, categories_id, doc_desc, critical_level, doc_type, created_by, created_at, updated_by, updated_at) FROM stdin;
    public               postgres    false    233   IM       #          0    16498    doc_history 
   TABLE DATA           w   COPY public.doc_history (doc_history_id, doc_id, action, action_by, action_detail, created_at, created_by) FROM stdin;
    public               postgres    false    230   �M       $          0    16507    doc_path 
   TABLE DATA           U   COPY public.doc_path (doc_path_id, doc_id, path, created_by, created_at) FROM stdin;
    public               postgres    false    231   �N       %          0    16516    doc_recipter 
   TABLE DATA           �   COPY public.doc_recipter (doc_recipter_id, doc_id, units_id, is_read, recip_status, created_by, created_at, recipter_desc) FROM stdin;
    public               postgres    false    232   �O       '          0    16537    page 
   TABLE DATA           ;   COPY public.page (page_id, page_no, page_name) FROM stdin;
    public               postgres    false    234   kP       (          0    16543 
   permission 
   TABLE DATA           ^   COPY public.permission (permission_id, units_id, page_id, created_at, created_by) FROM stdin;
    public               postgres    false    235   �P       )          0    16552    position 
   TABLE DATA           c   COPY public."position" (position_id, position_name, position_name_short, position_seq) FROM stdin;
    public               postgres    false    236   TQ       *          0    16558    units 
   TABLE DATA           �   COPY public.units (units_id, first_name, last_name, position_id, dept_id, post_code, address_detail, identify_id, status, is_active, img_path, identify_soldier_id, tel, blood_group, position_detail, created_at, created_by) FROM stdin;
    public               postgres    false    237   .R                  0    16471    users 
   TABLE DATA           v   COPY public.users (user_id, username, hashed_password, is_active, role, units_id, created_at, created_by) FROM stdin;
    public               postgres    false    227   �R       3           0    0    categories_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.categories_id_seq', 3, true);
          public               postgres    false    217            4           0    0    dept_dept_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.dept_dept_id_seq', 1, false);
          public               postgres    false    218            5           0    0    doc_history_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.doc_history_id_seq', 10, true);
          public               postgres    false    219            6           0    0 
   doc_id_seq    SEQUENCE SET     8   SELECT pg_catalog.setval('public.doc_id_seq', 2, true);
          public               postgres    false    222            7           0    0    doc_path_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.doc_path_id_seq', 2, true);
          public               postgres    false    220            8           0    0    doc_recipter_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.doc_recipter_id_seq', 7, true);
          public               postgres    false    221            9           0    0    page_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.page_id_seq', 6, true);
          public               postgres    false    223            :           0    0    permission_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.permission_id_seq', 1, true);
          public               postgres    false    224            ;           0    0    position_position_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.position_position_id_seq', 1, false);
          public               postgres    false    225            <           0    0    units_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.units_id_seq', 2, true);
          public               postgres    false    238            =           0    0    users_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_user_id_seq', 2, true);
          public               postgres    false    226            r           2606    16491    categories categories_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (categories_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public                 postgres    false    228            t           2606    16497    dept dept_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.dept
    ADD CONSTRAINT dept_pkey PRIMARY KEY (dept_id);
 8   ALTER TABLE ONLY public.dept DROP CONSTRAINT dept_pkey;
       public                 postgres    false    229            v           2606    16506    doc_history doc_history_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.doc_history
    ADD CONSTRAINT doc_history_pkey PRIMARY KEY (doc_history_id);
 F   ALTER TABLE ONLY public.doc_history DROP CONSTRAINT doc_history_pkey;
       public                 postgres    false    230            x           2606    16515    doc_path doc_path_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.doc_path
    ADD CONSTRAINT doc_path_pkey PRIMARY KEY (doc_path_id);
 @   ALTER TABLE ONLY public.doc_path DROP CONSTRAINT doc_path_pkey;
       public                 postgres    false    231            |           2606    16536    doc doc_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.doc
    ADD CONSTRAINT doc_pkey PRIMARY KEY (doc_id);
 6   ALTER TABLE ONLY public.doc DROP CONSTRAINT doc_pkey;
       public                 postgres    false    233            z           2606    16526    doc_recipter doc_recipter_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.doc_recipter
    ADD CONSTRAINT doc_recipter_pkey PRIMARY KEY (doc_recipter_id);
 H   ALTER TABLE ONLY public.doc_recipter DROP CONSTRAINT doc_recipter_pkey;
       public                 postgres    false    232            ~           2606    16542    page page_pkey 
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
       public                 postgres    false    237            n           2606    16483    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public                 postgres    false    227            p           2606    16485    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public                 postgres    false    227            !   4   x�3�|�c������`gÃ�F[��0���2Ƨ��"F��� �X*�      "   �   x���M
�0�יSx�BR.�a,�^@���v!.,/�yG1L5��.
�0�y�ތ5DA܉=�15o5�ĕ qf�^+'��pXX3�gV�$7%9Y�%�SR.�_�Q94����)-
߷��ln�����lCI4���~�ō��j���<�梭��,d����aa      &   �   x���1
AE�Sx���d3�q�b#���6;�{A��N�x�ŠX/����#��TN*G���C�ly�r�Ji�;��<U^V�q�ݫ\�}���[�6�È�D0̀zH=���)�$���a�� %.-r�u����Dn�fv4澣@�L~����b;      #   �   x���=N1�k�)ܥZ�3덽{�PP@��?	�hHP�	������V
RD��b�f��yC�d	�o!_�k�3��<�I��������9=�<B:O#�ز+-��ɵT�Λq<�޵y�g�d�=� ���_!���*�%�
�A�K����7�@uH,��sh��F�F�MgU�.��d�S:��ʙ�b�i�%���O�}���$���r��<����%ȷ��:�ÕLQ�=9�'      $   �   x���=
�@���S��쾼l�%M 
�?������B<�`��/����V�����W^m�źi���� G��\���� o�{�r�<S� W0nk�v��v9_)r�����s�E���	kR�{�����/��8KrWƜmU�r][���v^}      %   �   x��ѻ�@ ��7$��ϗ�i�T@&���S�C��S�m<
wGM$˲?ɶ>��
_���
���0���k���J��[����\A7U,X$p(�{�G��Ϲ�ְҡ�~�(M��5"�&̏�$*ZH���+�R��X�xt1k>i�?$�&|�w��#jr��j�����      '   �   x�}�;�`�g�. �y��@aF�Zu��@0�����4�X"���8C�?�M<�_�.�bR�(���"x���9��
����^g%ʭ/� �c}��U�|���v�����kԈ�~w�-�c��l�f6�4�c      (   F   x�3�4�4�44�20�20г43447�LL����2�C�rF@#r�@9cr&@9rf@93r1z\\\ ��#�      )   �   x�}�M�0�ם��a(�w�0�
`�.��5a��d���B)C\>��}o�����2]��L����VI�~wd�G��"�{���0��
+*�*��*��)�t-�>i�)d�ə��vC��q�ipoS�qe%�?�\c\F������t	�����gh��0��G�T��~nygz,n��5[�C��$�i��v ���#e      *   w   x�3�|�c��S�X�`��;f�pZr�r��!P	�042615�01C�3202�50"C+K+=cS##�����\.C�Ĕ��<(i��`d�f�������������=... �n:�          �   x�U�Ao�0 �s�;p����'��4�l��03�@�
JaP��׻��v��O�|W���X�}}�.�rk�g�i�}*����6h��qn��)�g�����Ś9v�?;&�#��'!�b%x0d�mlY��C&P��"E�#����1�I=d��4q��}u!�{8��Θ�U�d������#���A� \*I�7�����m$C�     