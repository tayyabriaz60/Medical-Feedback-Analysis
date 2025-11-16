# Render Connection Guide - Step by Step 🚀

## ✅ Code Status
- ✅ All code updated
- ✅ Pushed to GitHub: `tayyabriaz60/Deployment`
- ✅ Database URL auto-conversion ready

## 📋 Step 1: Render Dashboard Mein Jao

1. https://dashboard.render.com par jao
2. Login karo

## 📋 Step 2: New Web Service Create Karein

1. **"New +"** button → **"Web Service"**
2. **"Connect a repository"** → GitHub repository select karo
3. Repository: `tayyabriaz60/Deployment`
4. **"Connect"** click karo

## 📋 Step 3: Service Configuration

**Name:** `medical-feedback-platform`

**Region:** `Singapore` (ya apne location ke hisaab se)

**Branch:** `main`

**Root Directory:** (Leave empty)

**Runtime:** `Python 3`

**Build Command:**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command:**
```
uvicorn app.main:asgi_app --host 0.0.0.0 --port $PORT
```

## 📋 Step 4: Environment Variables Add Karein

**"Advanced"** section → **Environment Variables** add karo:

### Required Variables:

1. **SECRET_KEY**
   ```
   Key: SECRET_KEY
   Value: (PowerShell se generate karo)
   ```
   PowerShell command:
   ```powershell
   python -c "import secrets; print(secrets.token_urlsafe(64))"
   ```

2. **DATABASE_URL** ⭐ (IMPORTANT)
   ```
   Key: DATABASE_URL
   Value: postgresql://feedback_user:xyqi6PbqtYm8O0M4gGm8ZFbW3iJXDJQA@dpg-d4crlok9c44c7390icng-a/feedback_db_boli
   ```
   **Note:** Code automatically convert karega `postgresql+asyncpg://` format mein

3. **GOOGLE_API_KEY**
   ```
   Key: GOOGLE_API_KEY
   Value: (Apna Google Gemini API key)
   ```

4. **ADMIN_EMAIL**
   ```
   Key: ADMIN_EMAIL
   Value: aadmin@example.com
   ```

5. **ADMIN_PASSWORD**
   ```
   Key: ADMIN_PASSWORD
   Value: StrongPass123
   ```

### Optional Variables:

6. **PYTHON_VERSION**
   ```
   Key: PYTHON_VERSION
   Value: 3.11.9
   ```

7. **ENVIRONMENT**
   ```
   Key: ENVIRONMENT
   Value: production
   ```

8. **LOG_LEVEL**
   ```
   Key: LOG_LEVEL
   Value: INFO
   ```

9. **SQL_ECHO**
   ```
   Key: SQL_ECHO
   Value: false
   ```

10. **AUTO_OPEN_BROWSER**
    ```
    Key: AUTO_OPEN_BROWSER
    Value: 0
    ```

## 📋 Step 5: Deploy Karein

1. **"Create Web Service"** click karo
2. Build start hoga automatically
3. Wait karo (5-10 minutes)

## 📋 Step 6: Build Complete Hone Ke Baad

### Check Logs:
1. **"Logs"** tab click karo
2. Ye messages dhoondo:
   ```
   INFO - Database initialized
   INFO - Admin user created successfully
   INFO - Application startup complete
   ```

### Agar Admin User Create Nahi Hua:
Browser console (F12) mein:
```javascript
fetch(window.location.origin + '/auth/bootstrap-admin', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
})
.then(r => r.json())
.then(data => alert(JSON.stringify(data, null, 2)));
```

## 📋 Step 7: Login Karein

1. URL: `https://your-app.onrender.com/staff`
2. Email: `aadmin@example.com`
3. Password: `StrongPass123`
4. Login! ✅

## ✅ Important Notes

1. **DATABASE_URL:** Code automatically convert karega format
2. **Email:** `aadmin@example.com` (double 'a')
3. **Password:** Max 72 characters
4. **Build Time:** 5-10 minutes

## 🎯 Quick Checklist

- [ ] GitHub repository connected
- [ ] All environment variables set
- [ ] DATABASE_URL added
- [ ] Build successful
- [ ] Admin user created
- [ ] Login successful

Good luck! 🚀

