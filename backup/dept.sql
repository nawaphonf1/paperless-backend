PGDMP       '    
            }            units_manage    17.5    17.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16387    units_manage    DATABASE     �   CREATE DATABASE units_manage WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE units_manage;
                     postgres    false            �            1259    16389    dept    TABLE     �   CREATE TABLE public.dept (
    dept_id integer DEFAULT nextval('public.dept_dept_id_seq'::regclass) NOT NULL,
    dept_name character varying NOT NULL,
    dept_name_short character varying NOT NULL
);
    DROP TABLE public.dept;
       public         heap r       postgres    false            �          0    16389    dept 
   TABLE DATA           C   COPY public.dept (dept_id, dept_name, dept_name_short) FROM stdin;
    public               postgres    false    218   �       :           2606    16444    dept dept_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.dept
    ADD CONSTRAINT dept_pkey PRIMARY KEY (dept_id);
 8   ALTER TABLE ONLY public.dept DROP CONSTRAINT dept_pkey;
       public                 postgres    false    218            �   �   x���M
�0�יSx�BR.�a,�^@���v!.,/�yG1L5��.
�0�y�ތ5DA܉=�15o5�ĕ qf�^+'��pXX3�gV�$7%9Y�%�SR.�_�Q94����)-
߷��ln�����lCI4���~�ō��j���<�梭��,d����aa     