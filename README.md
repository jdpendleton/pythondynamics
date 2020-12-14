# Integrating Python with Microsoft Dynamics 365

## Why Python?

- Used by Data Analytics Professionals
- Libraries like Pandas, Numpy, PyPlot, Keras, and PySpark
- Taught to new developers in most CS programs
- Tools like iPython Notebooks to integrate with Jupyter Labs, Google Collab, and Zepl

## Getting Started

### What you will need

- Python (Anaconda)
- A Dynamics 365 Organization

### Registering your Python App with Dynamics 365

- Go to http://portal.azure.com and log in with your Dynamics 365 Account. Select **Azure Active Directory** from the menu.
  ![](Resources/AppRegistration1.jpg)

- Select **+ New registration**.
  ![](Resources/AppRegistration2.jpg)

- Enter a name for your python application and select **Register**.
  ![](Resources/AppRegistration3.jpg)

- Select **API Permissions** in your new app registration and select **+ Add a permission**. Select **Dynamics CRM** from the list.
  ![](Resources/AppRegistration4.jpg)

  > :information_source: **Note** Multiple API permissions point to https://admin.services.crm.dynamics.com/, such as Dynamics CRM and Common Data Service (soon to be Dataverse). Selecting any of these will work.

- Ensure **Delegated Permissions** is selected, **user_impersonation** is checked, and click **Add permissions**.
  ![](Resources/AppRegistration5.jpg)

- Select **Manifest** and ensure that `"allowPublicClient"` is set to `true`.
  ![](Resources/AppRegistration6.jpg)

- Select **Certificates and secrets** and select **+ New client secret** followed by the expiration and **Add**.
  ![](Resources/AppRegistration7.jpg)

- And that's it. All the information your Python needs to connect to your organization is on the **Overview** tab.
  ![](Resources/AppRegistration8.jpg)

### Creating An Application User

- Navigate to Security in your Dynamics Organization and select **Users**.
  ![](Resources/ApplicationUser1.jpg)

- Select the Application Users View and select **+ NEW**.
  ![](Resources/ApplicationUser2.jpg)

- Select the Application User Form and enter the required fields.
  ![](Resources/ApplicationUser3.jpg)

- The Application ID should match the Application ID from your App Registration in the Azure Portal.
  ![](Resources/ApplicationUser4.jpg)

- Assign the new user a security role. You can just copy the System Administrator role
  ![](Resources/ApplicationUser5.jpg)

## Using Python

- Refer to test.py and [brownbag.ipynb](brownbag.ipynb)
