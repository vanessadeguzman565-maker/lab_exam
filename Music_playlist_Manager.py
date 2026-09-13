class Song:
    def __init__(self, song_id, song_title, artist, duration):
        self.song_id = song_id
        self.title = song_title
        self.artist = artist
        self.duration = duration

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    # Add the beginning

    def insert_first(self, song):
        new_node = Node(song)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

        print("Song added at the beginning of the playlist.")

        # Add at the end

    def insert_last(self, song):
        
        new_node = Node(song)

        if self.is_empty():
            self.head = new_node

        else:
            current = self.head

            while current.next:
                current = current.next

        current.next = new_node

        self.size += 1

        print("Song added at the end of the playlist.")

        # Insert Song at the specific position

    def insert_at(self, song, position):

        if position < 1 or position > self.size + 1:
            print("Invalid position. Please enter a valid position.")
            return

        if position == 1:
            self.insert_first(song)
            return

            new_node = Node(song)
            current = self.head

            for i in range(1, position - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node

        self.size += 1

        print("Song inserted successfully.")

    # Display all songs

    def display(self):
        if self.is_empty():
            print("The playlist is empty.")
            return

        print("\n==== MUSIC PLAYLIST ====")

        current = self.head
        number = 1

        while current is not None:
            song = current.song
            print(f"\n Song #: {number}")
            print(f"Song ID: {song.song_id}")
            print(f"Song Title: {song.title}")
            print(f"Artist: {song.artist}")
            print(f"Duration: {song.duration}")

            current = current.next
            number += 1

    # Search for a song by ID

    def search(self, song_id):
        
        current = self.head

        while current is not None:
           
            if current.song.song_id == song_id:
                return current.song

            current = current.next

        return None

    # Remove a song by ID

    def delete(self, song_id):

        if self.head is None:

            print("The playlist is empty.")
            return

        if self.head.song.song_id == song_id:

            self.head = self.head.next
            self.size -= 1

            print("Song removed from the playlist.")
            return

            current = self.head

        while current.next is not None:

            if current.next.song.song_id == song_id:

                current.next = current.next.next
                self.size -= 1

                print("Song removed from the playlist.")
                return

            current = current.next

            print("Song not found in the playlist.")

    # Display

    def display_size(self):
        print(f"\nCurrent number of songs in the playlist: {self.size}")

def main():

    playlist = LinkedList()

    while True:

        print("\n================================")
        print("     MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at the Beginning")
        print("2. Add Song at the End")
        print("3. Insert Song at a Specific Position")
        print("4. Display All Songs")
        print("5. Search for a Song by ID")
        print("6. Remove a Song by ID")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":

            print("\n==== ADD SONG ====")

            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(song_id, song_title, artist, duration)
            playlist.insert_first(song)

        elif choice == "2":

            print("\n==== ADD SONG ====")

            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(song_id, song_title, artist, duration)
            playlist.insert_last(song)

        elif choice == "3":

            print("\n==== INSERT SONG ====")

            position = input("Enter the position to insert the song: ")
            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            while True:
                try:
                    position = int(input("Enter Position: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for position.")

            song = Song(song_id, song_title, artist, duration)

            playlist.insert_at(song, position)

        elif choice == "4":

            playlist.display()

        elif choice == "5":

            print("\n==== SEARCH SONG ====")

            song_id = input("Enter the Song ID to search: ")
            found_song = playlist.search(song_id)

            if found_song:
                print("\nSong Found:")
                print(f"Song ID: {found_song.song_id}")
                print(f"Song Title: {found_song.title}")
                print(f"Artist: {found_song.artist}")
                print(f"Duration: {found_song.duration}")
            else:
                print("\nSong not found in the playlist.")


        elif choice == "6":

            print("\n==== REMOVE SONG ====")

            song_id = input("Enter the Song ID to remove: ")

            playlist.delete(song_id)

        elif choice == "7":

            playlist.display_size()

        elif choice == "8":

            print("\nExiting the Music Playlist Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

main()

        
    