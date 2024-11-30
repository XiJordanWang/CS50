# Assets Management

#### Video Demo: [<https://youtu.be/VErhtEtI-RM>](<https://youtu.be/VErhtEtI-RM>)

#### Description:
The **Assets Management** system allows users to manage various assets, such as office furniture and equipment, in a database. The system includes the following key features:

1. **Viewing Assets:**
   - Users can view all assets in a list format. Each asset includes details such as the asset's ID, name, category, and value.

2. **Adding New Assets:**
   - Users can add new assets by filling out a form with the necessary asset details (e.g., name, category, and value). Once submitted, the asset is stored in the database.

3. **Deleting Assets:**
   - Each asset in the list includes a "Delete" button. Clicking this button removes the corresponding asset from the database. A confirmation prompt may appear before deletion to prevent accidental deletions.

---

### Features and Functions:

1. **View All Assets:**
   - Users can see a table listing all assets with their corresponding details (ID, name, category, value).
   - The assets are dynamically populated from the database.

2. **Add New Asset:**
   - A button labeled "Add Asset" allows users to open a form for adding new assets.
   - The form collects information such as the asset name, category, and value.
   - Upon form submission, the new asset is added to the database.

3. **Delete Asset:**
   - Each asset in the assets table includes a "Delete" button.
   - When clicked, a form sends a `POST` request with a hidden `_method` input set to `DELETE`, simulating the deletion of the asset.
   - Upon confirmation, the asset is removed from the database.

---

### Implementation Details:

1. **Add Asset Form:**
   - A form with fields for the asset's name, category, and value is provided for asset creation. The form sends a `POST` request to the `/add` route.

2. **Delete Asset Functionality:**
   - The deletion of assets is handled using a `POST` method override to simulate the `DELETE` request, which triggers the removal of the asset from the database.
   - After deletion, users are redirected back to the assets page.

3. **Backend:**
   - The system uses Flask as the backend framework and SQLAlchemy (or a similar SQL-based library) for database operations.
   - SQL queries are used to interact with the database for adding and deleting assets.

---

### Example Workflow:

1. **Viewing Assets:**
   - Navigate to the "Assets" page to view a list of all assets.
   - Each row in the table displays asset details along with an option to delete it.

2. **Adding an Asset:**
   - Click the "Add Asset" button to open the asset creation form.
   - Fill in the required details (name, category, value) and click "Submit" to add the asset.

3. **Deleting an Asset:**
   - To delete an asset, click the "Delete" button next to the asset in the list.
   - A confirmation is made before the asset is deleted from the database.

---

### Technologies Used:
- **Backend Framework**: Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS
- **Server**: Flask Development Server

---

### Future Improvements:
- Add user authentication for managing assets.
- Implement pagination for the asset list to handle large datasets.
- Allow asset updates (editing details of existing assets).