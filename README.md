# Book Covers

It all started with trying to add book cover images to my book database on [Coda](coda.io).

Turns out, book covers are annoying. There is no easy way to extract them out of GoodReads.

However, [openlibrary.org](openlibrary.org) comes to the rescue! OpenLibrary has a [simple search API](https://openlibrary.org/dev/docs/api/search), from which we can get the cover image, using their [covers API](https://openlibrary.org/dev/docs/api/covers).

The final challenge is getting the images to Coda. Fortunately, Coda can take any URL and treat it as an image URL. So all we have to do is construct the URL using the book title and author, fire a request to a simple Google Cloud Function that calls the API, and pipes the image data back to Coda, and voila!

This repo is the code for local testing. It needs some minor modifications to work as a Cloud Function -- just replace the @app.route with explicitly passing in the request object to the entry function, and you're good to go!

Happy book db building.
-Rushabh
