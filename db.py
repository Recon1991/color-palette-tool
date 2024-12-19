import sqlite3

def initialize_database():
    """Initializes the SQLite database and creates necessary tables."""
    connection = sqlite3.connect("color_palette.db")
    cursor = connection.cursor()

    # Create palettes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            colors TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    connection.commit()
    connection.close()

def save_palette(name, colors):
    """Saves a palette to the database.

    Args:
        name (str): Name of the palette.
        colors (list): List of color HEX codes.
    """
    connection = sqlite3.connect("color_palette.db")
    cursor = connection.cursor()

    # Convert the list of colors to a comma-separated string
    colors_str = ",".join(colors)

    cursor.execute('''
        INSERT INTO palettes (name, colors)
        VALUES (?, ?)
    ''', (name, colors_str))

    connection.commit()
    connection.close()

def get_all_palettes():
    """Retrieves all palettes from the database.

    Returns:
        list: List of palettes, where each palette is a dictionary with id, name, and colors.
    """
    connection = sqlite3.connect("color_palette.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT id, name, colors, created_at FROM palettes
    ''')
    rows = cursor.fetchall()

    palettes = [
        {"id": row[0], "name": row[1], "colors": row[2].split(","), "created_at": row[3]} 
        for row in rows
    ]

    connection.close()
    return palettes

def delete_palette(palette_id):
    """Deletes a palette from the database by ID.

    Args:
        palette_id (int): The ID of the palette to delete.
    """
    connection = sqlite3.connect("color_palette.db")
    cursor = connection.cursor()

    cursor.execute('''
        DELETE FROM palettes WHERE id = ?
    ''', (palette_id,))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
