# Bad Gateway Error - Fix Guide 🔧

## 🔍 What is Bad Gateway Error?

**Bad Gateway (502)** means:
- Application crashed or failed to start
- Service is restarting
- There's an error in the code preventing startup

---

## 📋 Step 1: Check Render Logs

### Render Dashboard:
1. **Render Dashboard** → **Web Service**
2. **"Logs"** tab click karo
3. **Scroll to bottom** (latest logs)
4. **Error messages** dhoondo

### Look for:
- ❌ **Import errors:** `ModuleNotFoundError`, `ImportError`
- ❌ **Syntax errors:** `SyntaxError`, `IndentationError`
- ❌ **Runtime errors:** `AttributeError`, `TypeError`
- ❌ **Startup errors:** Application failed to start

---

## 📋 Step 2: Common Issues & Fixes

### Issue 1: Import Error (bcrypt)
**Error:**
```
ModuleNotFoundError: No module named 'bcrypt'
```

**Fix:**
- `bcrypt>=4.0.0` already hai `requirements.txt` mein
- Build logs check karo - bcrypt install hua?

### Issue 2: Application Crash
**Error:**
```
Application startup failed
```

**Fix:**
- Logs mein exact error dekho
- Usually startup code mein issue hota hai

### Issue 3: Service Restarting
**Status:** Service restarting...

**Fix:**
- Wait karo (2-5 minutes)
- Service automatically restart hoga

---

## 📋 Step 3: Quick Fixes

### Fix 1: Manual Restart
1. Render Dashboard → Web Service
2. **"Manual Deploy"** → **"Deploy latest commit"**
3. Wait for build

### Fix 2: Check Build Logs
1. **"Logs"** tab → **"Build"** section
2. Check karo:
   - ✅ Build successful?
   - ❌ Build failed? (error dikhega)

### Fix 3: Check Runtime Logs
1. **"Logs"** tab → **"Runtime"** section
2. Check karo:
   - ✅ Application started?
   - ❌ Application crashed? (error dikhega)

---

## 📋 Step 4: Verify Code

### Check if code is correct:
1. **GitHub** par latest code check karo
2. **Render** latest commit deploy hua?
3. **Build successful** hua?

---

## 🔍 Debugging Steps

### Step 1: Check Latest Logs
Render logs mein ye dhoondo:

**✅ Success:**
```
INFO - Starting Medical Feedback Analysis Platform
INFO - Database initialized
INFO - Application startup complete
INFO - Uvicorn running on http://0.0.0.0:10000
```

**❌ Error:**
```
ERROR - ...
Traceback (most recent call last):
...
```

### Step 2: Check Build Status
**"Events"** tab mein check karo:
- ✅ Build successful
- ❌ Build failed (error dikhega)

### Step 3: Check Service Status
**Dashboard** mein service status:
- ✅ Live
- ⚠️ Building
- ❌ Failed

---

## 🚀 Quick Actions

### Action 1: Restart Service
1. Render Dashboard → Web Service
2. **"Manual Deploy"** → **"Deploy latest commit"**

### Action 2: Check Environment Variables
1. **Settings** → **Environment**
2. Verify:
   - `SECRET_KEY` set hai?
   - `DATABASE_URL` set hai?
   - `ADMIN_EMAIL` set hai?
   - `ADMIN_PASSWORD` set hai?

### Action 3: Rollback (If needed)
1. **"Events"** tab
2. Previous successful deploy dhoondo
3. **"Redeploy"** click karo

---

## 📝 What to Share

Agar issue persist kare, to mujhe ye share karo:

1. **Latest logs** (last 50-100 lines)
2. **Build logs** (agar build fail hua)
3. **Error message** (exact error)
4. **Service status** (Live/Building/Failed)

---

## ✅ Expected After Fix

Service should show:
- ✅ Status: **Live**
- ✅ URL accessible
- ✅ No Bad Gateway error

---

## 🎯 Quick Checklist

- [ ] Render logs check kiye
- [ ] Build successful hai?
- [ ] Application started hai?
- [ ] Environment variables set hain?
- [ ] Latest code deployed hai?

Good luck! 🚀

