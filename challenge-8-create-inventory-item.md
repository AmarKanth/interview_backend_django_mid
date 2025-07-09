## Challenge 8: Create Inventory Item — Explanation

### Objective
Users need to be able to **add an item to the Inventory through the API**, which means need an endpoint 
that can receive data and save a new inventory item to the database.

In addition to basic fields, each inventory item will include a **metadata object** that contains:
- `year`
- `actors`
- `imdb_rating`
- `rotten_tomatoes_rating`
- `film_locations`

### Steps to Create the Inventory Section
1. **Create the Inventory Model**
   - Define the `Inventory` model with the following fields:
     - `title`: A short text field for the name of the inventory item.
     - `created_at`: A timestamp automatically set when the item is created.
     - `metadata`: A `JSONField` to store structured data like year, actors, ratings, and locations.

2. **Apply Migrations**
   - Generate the migration file:
     ```bash
     python manage.py makemigrations inventory
     ```
   - Apply the migration changes to the database:
     ```bash
     python manage.py migrate
     ```

3. **Create the Serializer**
   - In the `inventory/serializers.py` file, define a serializer for the `Inventory` model.
   - Use `ModelSerializer` so that validation is automatically handled based on the model’s field definitions.

4. **Create the Api**
   - Create an endpoint using Django REST Framework’s `APIView` class.
   - Use the `POST` HTTP method to receive and save the inventory data.
   - Return `HTTP_201_CREATED` on successful creation.
   - If validation fails, return `HTTP_400_BAD_REQUEST` with serializer error details.

5. **Update `urls.py` File**
   - Add a URL pattern for the Inventory POST request.

6. **Example cURL Request to Add an Inventory Item**
   ```bash
   curl -X POST http://localhost:8000/inventory/create/ \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Inception",
       "metadata": {
         "year": 2010,
         "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
         "imdb_rating": 8.8,
         "rotten_tomatoes_rating": 87,
         "film_locations": ["Los Angeles", "Paris", "Tokyo"]
       }
     }'
    ```

7. **Expected Response**
   ```
   {
      "id": 1,
      "title": "Inception",
      "created_at": "2025-07-09T14:35:27.123456Z",
      "metadata": {
          "year": 2010,
          "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
          "imdb_rating": 8.8,
          "rotten_tomatoes_rating": 87,
          "film_locations": ["Los Angeles", "Paris", "Tokyo"]
      }
    }
   ```
