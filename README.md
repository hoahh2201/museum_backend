<!-- The core Firebase JS SDK is always required and must be listed first -->
<script src="https://www.gstatic.com/firebasejs/7.3.0/firebase-app.js"></script>

<!-- TODO: Add SDKs for Firebase products that you want to use
     https://firebase.google.com/docs/web/setup#available-libraries -->
<script src="https://www.gstatic.com/firebasejs/7.3.0/firebase-analytics.js"></script>

<script>
  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyA0D97G56fESEXG7VByJWVNGkwFIZoq55E",
    authDomain: "museumtale.firebaseapp.com",
    databaseURL: "https://museumtale.firebaseio.com",
    projectId: "museumtale",
    storageBucket: "museumtale.appspot.com",
    messagingSenderId: "972171369468",
    appId: "1:972171369468:web:c3bd5d157c0f83b24af079",
    measurementId: "G-CL3L2STT97"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
</script>


export GCS_BUCKET="museum_tale"
export GCP_PROJECT="museumtale"
export FIREBASE_CONFIG="firebase_config.json"