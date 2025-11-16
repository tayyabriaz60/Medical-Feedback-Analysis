// Copy this code and paste in browser console (F12) on https://deployment-00vv.onrender.com

fetch('https://deployment-00vv.onrender.com/auth/bootstrap-admin', {
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
    alert('⚠️ Response: ' + JSON.stringify(data, null, 2));
  }
})
.catch(err => {
  console.error('❌ Error:', err);
  alert('❌ Error: ' + err.message + '\n\nCheck browser console for details.');
});

