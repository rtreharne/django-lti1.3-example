# Django LTI 1.3 Base Tool

This is a minimal Django-based LTI 1.3 tool designed for development and
testing against Canvas LMS (or any LTI-compliant VLE).\
It includes:

-   OIDC login initiation\
-   LTI launch validation\
-   JWKS endpoint\
-   Minimal landing page showing user + course data\
-   Claims inspection table

------------------------------------------------------------------------

## 🚀 Quick Start

### 1. Clone the repository

    git clone git@github.com:rtreharne/django-lti1.3-example.git
    cd django-lti1.3-example

------------------------------------------------------------------------

## 🔑 2. Generate RSA Keys for LTI

The tool requires an RSA private/public keypair to sign LTI messages.

Run the following:

``` bash
mkdir -p lti_keys
openssl genrsa -out lti_keys/private.pem 2048
openssl rsa -in lti_keys/private.pem -pubout -out lti_keys/public.pem
```

Ensure these keys are **NOT committed to git** --- they are already
ignored in `.gitignore`.

------------------------------------------------------------------------

## ⚙️ 3. Environment Settings

Set your environment variables in `.env` (or directly in `settings.py`
for dev).

For use with a development instance of the Canvas LMS you'll need at least:

    LTI_CLIENT_ID=XXXXX
    LTI_DEPLOYMENT_ID=XXXXX
    LTI_TOOL_REDIRECT_URI=http://localhost:8000/launch/
    LTI_ISS=https://canvas.instructure.com
    LTI_PLATFORM_JWKS_URL=http://canvas.docker/api/lti/security/jwks
    LTI_AUTHORIZE_URL=http://canvas.docker/api/lti/authorize_redirect

------------------------------------------------------------------------

## 🧩 4. Start Django

    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

------------------------------------------------------------------------

## ▶️ 5. Register Your Tool in Canvas (Developer Key + Course Installation)

To use your Django LTI 1.3 Base Tool inside Canvas, you must:

1. Create an **LTI 1.3 Developer Key**
2. Install the tool into a **Canvas course**
3. Launch the tool to verify everything works

Below is the full setup guide.

---

## **A. Create the LTI 1.3 Developer Key**

In Canvas:

1. Go to **Admin → Developer Keys**
2. Click **+ Developer Key → LTI Key**
3. Using **Manual Entry** fill in:

### **1. Key Settings**

| Setting | Value |
|--------|--------|
| **Key Name** | Django LTI 1.3 Base Tool |
| **Owner Email** | your email |
| **Redirect URIs** | `http://localhost:8000/launch/` |
| **Privacy Level** | Public (recommended) |

---

### **2. LTI Advantage Services (Optional)**

Enable only if needed:

- Names & Role Provisioning
- Assignment & Grade Services
- Deep Linking

Your base tool works without these.

---

### **3. Additional Settings → LTI Key Configuration**


| Setting | Value |
|--------|--------|
| **OIDC Login URL** | `http://localhost:8000/login/` |
| **Target Link URI** | `http://localhost:8000/launch/` |
| **JWKS URL** | `http://localhost:8000/jwks/` |

---

### **4. Save the Developer Key**

After saving:

- Toggle the key **ON** (green)
- Copy the **Client ID**

---

## **B. Install the Tool into a Canvas Course**

1. Go to **Courses → Your Course**
2. Click **Settings → Apps**
3. Click **+ App**
4. For **Configuration Type**, choose:

> **By Client ID**

5. Paste the **Client ID** from the Developer Key
6. Canvas will display the tool name and settings
7. Click **Install**

The tool is now installed in that course.

---

## **C. Launch the Tool**

Your tool may appear in:

- Course **Navigation**
- **Modules** (if added as a module item)
- **Assignments** (if A+GS or deep linking enabled)

For a simple launch:

1. Go to the course
2. Open the left-hand menu
3. Click **Django LTI 1.3 Base Tool**

Canvas will:

- Send the user to `/login/`
- Redirect via OIDC to Canvas
- POST an `id_token` to `/launch/`
- Your tool validates signature, state, nonce, issuer, audience
- User lands on `/landing/`

You should see:

- “Welcome, \<Given Name\>”
- Course title
- Full LTI claims table

---

## 📚 Canvas Documentation & GitHub Resources

### **Official Canvas Documentation**

- LTI 1.3 Dev Key config  
  https://canvas.instructure.com/doc/api/file.lti_dev_key_config.html  
- LTI Deep Linking  
  https://canvas.instructure.com/doc/api/file.lti_deep_linking.html  
- LTI Advantage Services  
  https://canvas.instructure.com/doc/api/lti_api.html  
- Authentication & OAuth  
  https://canvas.instructure.com/doc/api/file.oauth.html  

### **Canvas LMS GitHub**

- Main Canvas LMS repo  
  https://github.com/instructure/canvas-lms  
- LTI models & implementation  
  https://github.com/instructure/canvas-lms/tree/master/app/models/lti  
- IMS/LTI security code  
  https://github.com/instructure/canvas-lms/tree/master/app/models/lti/ims  

### **LTI Standard (IMS Global / 1EdTech)**

- LTI 1.3 Core Specification  
  https://www.imsglobal.org/spec/lti/v1p3  
- LTI Advantage  
  https://www.imsglobal.org/spec/lti/v1p3/  

------------------------------------------------------------------------

## ✔️ 6. Launch Flow

Canvas → `/login/` → redirects to Canvas OIDC → Canvas posts `id_token`
→ `/launch/`.

The tool then:

1.  Validates the JWT signature using Canvas's JWKS\
2.  Validates issuer, audience, nonce, state\
3.  Extracts user & course data\
4.  Stores claims in session\
5.  Redirects to `/landing/`

------------------------------------------------------------------------

## 🎛️ 7. Landing Page

Displays:

-   Logged-in user's given name
-   Course title
-   A full expandable LTI claims table

Useful for debugging and verifying launches.

------------------------------------------------------------------------

## 🧪 8. Testing Cookies in Cross‑Site Contexts

Endpoints:

-   `/test_set/`
-   `/test_read/`

These demonstrate session persistence in Firefox and Chrome during LTI
launches.

------------------------------------------------------------------------

## 📁 Project Structure

    tool/
        views.py
        urls.py
        templates/
    lti/
        settings.py
    lti_keys/
        private.pem
        public.pem
    manage.py

------------------------------------------------------------------------

## 📜 License

This project is licensed under the [MIT License](LICENSE).

------------------------------------------------------------------------

## 👤 Author

**Dr. Robert Treharne**
