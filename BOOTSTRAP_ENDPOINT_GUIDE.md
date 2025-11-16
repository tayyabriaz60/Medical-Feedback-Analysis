# Bootstrap Endpoint Run Karne Ka Guide 🚀

## Method 1: Browser Console (Easiest) ✅

### Step 1: App URL Kholo
1. Browser mein jao: `https://your-app.onrender.com`
   - Ya jo bhi Render URL hai (e.g., `https://deployment-18e3.onrender.com`)

### Step 2: Browser Console Kholo
- **Windows/Linux:** Press `F12` ya `Ctrl + Shift + J`
- **Mac:** Press `Cmd + Option + J`
- Ya **Right-click** → **"Inspect"** → **"Console"** tab

### Step 3: Code Paste Karo
Console mein ye code paste karo (apne URL ke saath):

```javascript
fetch('https://your-app.onrender.com/auth/bootstrap-admin', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
})
.then(r => r.json())
.then(data => {
  console.log('✅ Result:', data);
  if (data.message && data.message.includes('created')) {
    alert('✅ Admin user created successfully!\n\nEmail: ' + data.email + '\n\nAb login kar sakte ho!');
  } else if (data.message && data.message.includes('already exists')) {
    alert('ℹ️ Admin user already exists.\n\nEmail: ' + data.email + '\n\nAb login kar sakte ho!');
  } else {
    alert('⚠️ Response:\n\n' + JSON.stringify(data, null, 2));
  }
})
.catch(err => {
  console.error('❌ Error:', err);
  alert('❌ Error: ' + err.message);
});
```

**Important:** `https://your-app.onrender.com` ko apne actual Render URL se replace karo!

### Step 4: Enter Press Karo
- Code paste karne ke baad **Enter** press karo
- Result console aur alert mein dikhega

---

## Method 2: API Docs Se (Visual) 📖

### Step 1: API Docs Kholo
1. Browser mein jao: `https://your-app.onrender.com/docs`
   - Ya `https://your-app.onrender.com` par `/docs` add karo

### Step 2: Bootstrap Endpoint Dhoondo
1. Page scroll karo
2. **`/auth/bootstrap-admin`** endpoint dhoondo
3. Endpoint expand karo (click karo)

### Step 3: Execute Karo
1. **"Try it out"** button click karo
2. **"Execute"** button click karo
3. Response dekho

### Expected Response:
```json
{
  "message": "Admin user created successfully",
  "email": "admin@example.com",
  "role": "admin",
  "id": 1
}
```

---

## Method 3: Postman/Thunder Client (Advanced) 🔧

### Postman:
1. **New Request** create karo
2. **Method:** `POST`
3. **URL:** `https://your-app.onrender.com/auth/bootstrap-admin`
4. **Headers:** 
   - `Content-Type: application/json`
5. **Send** click karo

### Thunder Client (VS Code):
1. VS Code mein Thunder Client extension install karo
2. **New Request** create karo
3. **Method:** `POST`
4. **URL:** `https://your-app.onrender.com/auth/bootstrap-admin`
5. **Send Request** click karo

---

## Method 4: curl Command (Terminal) 💻

### Windows PowerShell:
```powershell
Invoke-WebRequest -Uri "https://your-app.onrender.com/auth/bootstrap-admin" -Method POST -ContentType "application/json"
```

### Linux/Mac Terminal:
```bash
curl -X POST "https://your-app.onrender.com/auth/bootstrap-admin" \
  -H "Content-Type: application/json"
```

---

## ✅ Success Response

### Admin User Created:
```json
{
  "message": "Admin user created successfully",
  "email": "admin@example.com",
  "role": "admin",
  "id": 1
}
```

### Admin User Already Exists:
```json
{
  "message": "Admin user already exists",
  "email": "admin@example.com",
  "role": "admin",
  "id": 1
}
```

---

## ❌ Error Responses

### Environment Variables Not Set:
```json
{
  "detail": "ADMIN_EMAIL and ADMIN_PASSWORD environment variables must be set"
}
```
**Fix:** Render environment variables check karo

### Users Already Exist:
```json
{
  "detail": "Users already exist (1). Cannot bootstrap admin. Existing users: admin@example.com"
}
```
**Fix:** Direct login try karo (admin user already hai)

---

## 🎯 Quick Copy-Paste Code (Browser Console)

Apne Render URL ke saath:

```javascript
// Replace 'your-app' with your actual Render app name
const APP_URL = 'https://deployment-18e3.onrender.com'; // CHANGE THIS!

fetch(APP_URL + '/auth/bootstrap-admin', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
})
.then(r => r.json())
.then(data => {
  console.log('✅ Result:', data);
  alert(JSON.stringify(data, null, 2));
})
.catch(err => {
  console.error('❌ Error:', err);
  alert('Error: ' + err.message);
});
```

---

## 📋 Step-by-Step (Easiest Method)

1. ✅ Browser kholo
2. ✅ App URL par jao: `https://your-app.onrender.com`
3. ✅ `F12` press karo (console kholo)
4. ✅ Console tab select karo
5. ✅ Code paste karo (URL update karke)
6. ✅ Enter press karo
7. ✅ Result dekho

---

## 🔍 Troubleshooting

### Error: "Failed to fetch"
- **Fix:** URL sahi hai? Internet connection hai?

### Error: "404 Not Found"
- **Fix:** URL sahi hai? `/auth/bootstrap-admin` endpoint available hai?

### Error: "CORS error"
- **Fix:** Same origin se request kar rahe ho? (app URL se hi)

---

## 💡 Tips

1. **Browser Console** sabse easy method hai
2. **API Docs** visual method hai (better for beginners)
3. **URL exact** hona chahiye
4. **No body needed** - POST request empty body ke saath

---

## 🚀 Ready to Go!

Ab bootstrap endpoint run karo aur admin user create karo! ✅

Good luck! 🎉

