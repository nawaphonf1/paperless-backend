PGDMP      '    
            }            units_manage    17.5    17.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16387    units_manage    DATABASE     �   CREATE DATABASE units_manage WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE units_manage;
                     postgres    false            �            1259    16419    position    TABLE     �   CREATE TABLE public."position" (
    position_id integer DEFAULT nextval('public.posotion_position_id_seq'::regclass) NOT NULL,
    position_name character varying NOT NULL,
    position_name_short character varying NOT NULL,
    position_seq integer
);
    DROP TABLE public."position";
       public         heap r       postgres    false            �          0    16419    position 
   TABLE DATA           c   COPY public."position" (position_id, position_name, position_name_short, position_seq) FROM stdin;
    public               postgres    false    226   E       :           2606    16452    position position_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (position_id);
 B   ALTER TABLE ONLY public."position" DROP CONSTRAINT position_pkey;
       public                 postgres    false    226            �   �   x�}�M�0�ם��a(�w�0�
`�.��5a��d���B)C\>��}o�����2]��L����VI�~wd�G��"�{���0��
+*�*��*��)�t-�>i�)d�ə��vC��q�ipoS�qe%�?�\c\F������t	�����gh��0��G�T��~nygz,n��5[�C��$�i��v ���#e     