--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: jobs; Type: TABLE; Schema: public; Owner: mg
--

CREATE TABLE public.jobs (
    id integer NOT NULL,
    user_id integer,
    company character varying(50),
    role character varying(50),
    pay integer,
    link text,
    app_date text,
    contact_name character varying(50),
    contact_details character varying(50),
    app_response character varying(30),
    interview_stage character varying(30),
    interview_details text,
    offer boolean
);


ALTER TABLE public.jobs OWNER TO mg;

--
-- Name: jobs_id_seq; Type: SEQUENCE; Schema: public; Owner: mg
--

CREATE SEQUENCE public.jobs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.jobs_id_seq OWNER TO mg;

--
-- Name: jobs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mg
--

ALTER SEQUENCE public.jobs_id_seq OWNED BY public.jobs.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: mg
--

CREATE TABLE public.users (
    id integer NOT NULL,
    first_name character varying(20),
    last_name character varying(20),
    email text,
    password character varying(64),
    admin boolean
);


ALTER TABLE public.users OWNER TO mg;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: mg
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO mg;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: mg
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: jobs id; Type: DEFAULT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.jobs ALTER COLUMN id SET DEFAULT nextval('public.jobs_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: jobs; Type: TABLE DATA; Schema: public; Owner: mg
--

COPY public.jobs (id, user_id, company, role, pay, link, app_date, contact_name, contact_details, app_response, interview_stage, interview_details, offer) FROM stdin;
5	1	Apple	Junior WebDev	75000	www.apple.com	2022-01-13	Tim Cook	tim@apple.com	Positive Email	3rd Face to Face	2022-01-10	t
2	1	Facebook	Junior WebDev	75000	www.facebook.com	2022-01-19	Mark Zuckerberg	mark@facebook.com	Positive Email	2nd Face to Face	2022-01-17	f
3	1	Amazon	Junior WebDev	88000	www.amazon.com	2022-01-11	Jeff Bezos	jeff@amazon.com	Positive phonecall	2nd Face to Face	2022-01-20	f
1	1	Google	Junior WebDev	65000	www.google.com	2022-01-10	Sundar Pichai	sundar@google.com	no response	1st Face to Face	2022-01-18	f
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: mg
--

COPY public.users (id, first_name, last_name, email, password, admin) FROM stdin;
1	Matt	Graham	iam@mattgrah.am	$2b$12$yt8InAQo9GxN1.N1fhjNRO1kFp/t826/Ti7na393MRsqIbQnv2LFm	t
\.


--
-- Name: jobs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mg
--

SELECT pg_catalog.setval('public.jobs_id_seq', 11, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: mg
--

SELECT pg_catalog.setval('public.users_id_seq', 14, true);


--
-- Name: jobs jobs_pkey; Type: CONSTRAINT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT jobs_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: jobs fk_user; Type: FK CONSTRAINT; Schema: public; Owner: mg
--

ALTER TABLE ONLY public.jobs
    ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

