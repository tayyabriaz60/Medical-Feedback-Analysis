# Render Console/Logs Check Karne Ka Guide 🔍

## Step 1: Render Logs Kholo

1. **Render Dashboard** mein jao: https://dashboard.render.com
2. Apna **Web Service** select karo (`medical-feedback-platform` ya jo name hai)
3. **"Logs"** tab click karo
4. **Scroll up** karo startup logs tak

---

## Step 2: Startup Logs Check Karo

### ✅ Success Signs (Ye Dikhna Chahiye):

```
INFO - Starting Medical Feedback Analysis Platform
INFO - Database schema ensured
INFO - Database initialized
INFO - Creating initial admin user: aadmin@example.com
INFO - Admin user created successfully: aadmin@example.com (ID: 1)
INFO - Admin bootstrap executed
INFO - Application startup complete
```

### ❌ Error Signs (Ye Dikhe To Problem Hai):

#### Error 1: Admin Bootstrap Failed
```
ERROR - Admin bootstrap failed: password cannot be longer than 72 bytes
```
**Solution:** Password 72 characters se kam karo

#### Error 2: Environment Variables Missing
```
INFO - Admin bootstrap skipped - ADMIN_EMAIL or ADMIN_PASSWORD not set
```
**Solution:** Render environment variables check karo

#### Error 3: Database Connection Error
```
ERROR - Database connectivity check failed
```
**Solution:** DATABASE_URL check karo

---

## Step 3: Specific Errors Check Karo

### A. Admin Bootstrap Error?

**Logs mein dhoondo:**
- `Admin bootstrap failed`
- `Failed to create admin user`
- `password cannot be longer than 72 bytes`

**Agar ye dikhe:**
1. Render Dashboard → Environment
2. `ADMIN_PASSWORD` check karo (max 72 chars)
3. Update karo agar zyada hai
4. Redeploy karo

### B. Environment Variables Missing?

**Logs mein dhoondo:**
- `Admin bootstrap skipped - ADMIN_EMAIL or ADMIN_PASSWORD not set`

**Agar ye dikhe:**
1. Render Dashboard → Environment
2. Check karo:
   - `ADMIN_EMAIL` = `aadmin@example.com`
   - `ADMIN_PASSWORD` = `StrongPass123`
3. Agar missing hain, add karo
4. Service automatically redeploy hoga

### C. Database Error?

**Logs mein dhoondo:**
- `Database connectivity check failed`
- `Connection refused`
- `ModuleNotFoundError: No module named 'psycopg2'`

**Agar ye dikhe:**
1. `DATABASE_URL` check karo
2. Database service running hai?
3. URL format sahi hai?

---

## Step 4: Complete Logs Copy Karo

Agar error hai, to:

1. Render Logs tab mein
2. **"Download Logs"** ya **"Copy"** button use karo
3. Ya manually select karo aur copy karo
4. Mujhe share karo

---

## Common Errors & Solutions

### Error: "Admin bootstrap failed: password cannot be longer than 72 bytes"

**Fix:**
1. Render Dashboard → Environment
2. `ADMIN_PASSWORD` ko shorten karo (max 72 chars)
3. Save karo
4. Service auto-redeploy hoga

### Error: "Admin bootstrap skipped - ADMIN_EMAIL or ADMIN_PASSWORD not set"

**Fix:**
1. Render Dashboard → Environment
2. Add karo:
   - Key: `ADMIN_EMAIL`, Value: `aadmin@example.com`
   - Key: `ADMIN_PASSWORD`, Value: `StrongPass123`
3. Save karo

### Error: "Users already exist (X). Cannot bootstrap admin."

**Fix:**
- Ye error bootstrap endpoint se aayega
- Matlab admin user already hai
- Direct login try karo

---

## Quick Check Commands

### Browser Console Se Check Karo:

```javascript
// Check if admin user exists
fetch('https://deployment-00vv.onrender.com/auth/bootstrap-admin', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
})
.then(r => r.json())
.then(data => {
  console.log('Bootstrap Result:', data);
  if (data.message && data.message.includes('already exists')) {
    console.log('✅ Admin user exists!');
  } else if (data.message && data.message.includes('created')) {
    console.log('✅ Admin user created!');
  } else {
    console.log('⚠️ Issue:', data);
  }
});
```

---

## What to Share

Agar error hai, to mujhe ye share karo:

1. **Startup logs** (application start hote waqt)
2. **Admin bootstrap logs** (agar dikhe)
3. **Any error messages** (red text)
4. **Last 50-100 lines** of logs

---

## Expected Startup Flow

```
1. INFO - Starting Medical Feedback Analysis Platform
2. INFO - Database schema ensured
3. INFO - Database initialized
4. INFO - Creating initial admin user: aadmin@example.com
5. INFO - Admin user created successfully: aadmin@example.com (ID: 1)
6. INFO - Admin bootstrap executed
7. INFO - Application startup complete
8. INFO - Uvicorn running on http://0.0.0.0:10000
```

Agar ye sab dikhe, to admin user create ho gaya hai! ✅

---

## Next Steps

1. ✅ Logs check karo
2. ✅ Error identify karo (agar hai)
3. ✅ Fix apply karo
4. ✅ Bootstrap endpoint try karo (agar admin user nahi bana)
5. ✅ Login try karo

Good luck! 🚀

