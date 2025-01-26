class BookDetails {
    private $title;
    private $author;

    public function __construct($title, $author) {
        $this->title = $title;
        $this->author = $author;
    }

    public function getTitle() {
        return $this->title;
    }

    public function getAuthor() {
        return $this->author;
    }
}

class BookState {
    private $currentPage;

    public function turnPage() {
        // Logic to turn to the next page
    }

    public function getCurrentPage() {
        return "current page content"; 
    }
}

class BookLocation {
    public function getLocation() {
        // Logic to return the position in the library
    }
}

class BookStorage {
    private $bookDetails;

    public function __construct(BookDetails $bookDetails) {
        $this->bookDetails = $bookDetails;
    }

    public function save() {
        $filename = '/documents/' . $this->bookDetails->getTitle() . ' - ' . $this->bookDetails->getAuthor();
        file_put_contents($filename, serialize($this));
    }
}

interface Printer {
    public function printPage($page);
}

class PlainTextPrinter implements Printer {
    public function printPage($page) {
        echo $page;
    }
}

class HtmlPrinter implements Printer {
    public function printPage($page) {
        echo '<div style="single-page">' . $page . '</div>';
    }
}
