from supabase import create_client

SUPABASE_URL = "https://ccwtgzpaobpjvmiddvfq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNjd3RnenBhb2JwanZtaWRkdmZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE4Nzc1MzYsImV4cCI6MjA2NzQ1MzUzNn0.SzXTXhTaB7OHve3EKcLC51tSke0058z_y-CskWittLk"  # anon key ที่คุณมีอยู่

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
