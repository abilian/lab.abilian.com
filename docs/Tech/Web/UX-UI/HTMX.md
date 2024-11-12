(Based on a talk given at OSXP 2023).

HTMX has emerged, over the last couple of years, as a truly disruptive way to create web applications, bridging the gap between classical web principles and the demands of modern web applications. HTMX revisits the foundational concepts of hypermedia, integrating them seamlessly with contemporary development practices. This unique blend positions HTMX as a "neo-classical" tool, offering a revolutionary approach to building web applications that are both dynamic and efficient.

HTMX's philosophy based on the principle of enhancing HTML with capabilities that traditionally required complex JavaScript or full-fledged frontend frameworks. By doing so, it champions a return to the basics of the web—leveraging the power of hypermedia to drive application state and user interaction. This approach reminds of the early days of the web when simplicity and directness guided development. Yet, HTMX injects a fresh breath of innovation into this paradigm, enabling developers to create rich, interactive web experiences without departing from the core principles that made the web universally accessible.

## Understanding Hypermedia Applications

A hypermedia application is a system that uses hypermedia as the engine of application state. Beyond common perception, JSON APIs are not the entirety of hypermedia systems. "Hypermedia" refers to digital content incorporating various media types—text, images, video, and links—interconnected in a non-linear manner.

## The Journey of Hypermedia Applications

The history of hypermedia applications dates back to the early days of the internet, where the Web was primarily a space for static information. With the advent of technologies like HTML, CSS, and JavaScript, these applications began to evolve into more dynamic and interactive forms.

### The Early Web

In the 1990s, web specialists, then known as "webmasters," focused on creating static websites. These sites were mainly composed of HTML documents linked by hyperlinks, forming the basis of the first hypermedia applications.

### The Era of Proprietary Technologies

From 1996 to 2005, new proprietary technologies such as ActiveX, Java applets, Flash, and Silverlight emerged. These technologies introduced a distinction between applications and websites, laying the groundwork for rich Web interactions.

### Web 2.0 and the Rise of AJAX

The introduction of jQuery and AJAX ("Asynchronous JavaScript and XML") in the 2000s marked a significant transformation of the Web. The depreciation of ActiveX and Flash, especially after their lack of support on the iPhone, pushed developers to recreate rich applications using HTML, CSS, and JS.

### The Advent of SPAs

Between 2010 and 2020, the world witnessed the rise of single-page applications (SPAs), thanks to the widespread adoption of HTML5, CSS3, and ES5. This period also marked the beginning of the shift in Web traffic towards mobile devices and the introduction of frameworks like Angular, React, and Vue.

## The Current Context

Since 2020, SPA applications dominate the Web landscape, with traditional frameworks increasingly focusing on delivering JSON to browsers. Meanwhile, a question arises: Is it time to return to the fundamental principles of hypermedia?

# HTMX: Redefining Web Development

As the digital landscape rapidly evolves, HTMX emerges as an innovative response to the challenges posed by complex SPA architectures. Developed by Carson Gross in 2020, HTMX is a lightweight JavaScript library that revitalizes the hypermedia approach in modern web development.

## What is HTMX?

HTMX is a 15 kB (compressed) library with no dependencies that facilitates the implementation of hypermedia-driven applications. It enables static web pages to be enriched with dynamic interactions without requiring excessive JavaScript complexity.

### Key Features of HTMX

1. **Extended HTTP Requests**: HTMX extends the ability of HTML elements to perform HTTP requests, beyond traditional GET and POST methods, including PUT, PATCH, and DELETE.

2. **Various Event Triggers**: With HTMX, different browser events can trigger actions, offering greater interactivity within web applications.

3. **Selective Page Updating**: HTMX allows replacing any part of a web page, instead of reloading the entire page, thus improving the user experience.

## How to Use HTMX?

Implementing HTMX is remarkably straightforward. It involves integrating the library via a script link and then using special attributes in HTML code to activate its features.

### Usage Example

```html
<script src="https://unpkg.com/htmx.org@latest"></script>

<button hx-get="/contacts" hx-target="#contacts">
  Get Contacts
</button>
```

In this example, a button is used to send a GET request to a server and update a specific part of the page with the response.

## HTMX Adoption

HTMX's appeal lies in its ability to simplify the development of modern, responsive user interfaces. By providing access to functionalities such as AJAX, CSS transitions, browser history, WebSockets, and Server Sent Events directly in HTML, HTMX enables the construction of sophisticated user interfaces with the simplicity and power of hypertext.

# Real-World Experiences and Recommendations on HTMX

The adoption of HTMX in web development has generated significant feedback, highlighting its impact on simplifying processes and the efficiency of web applications.

## Concrete Case Studies

### Contexte (2022)

A project to redesign an application revealed remarkable results after adopting HTMX. The code size was reduced by 67%, while the initial loading time and application memory usage were also significantly improved. These improvements demonstrate HTMX's efficiency in resource management and performance.

### OpenUnited (2023)

OpenUnited's experience with HTMX led to a 61% reduction in the application's code size. Developers reported a subjective acceleration in development speed, estimated to be about five times faster. This case study underscores HTMX's effectiveness in reducing the complexity of web development.

## Recommendations

### When to Use HTMX

- **For Low-Interactivity Sites**: HTMX excels in contexts where interactions are predominantly based on text and images, such as e-commerce sites or information platforms.
- **Server-Side Advantage**: HTMX is particularly suited for applications that rely on server-side data processing and analysis.
- **Large Data Transfers**: HTMX is effective in scenarios where the response to a request returns a complete HTML document, optimizing data transfer.

### When Not to Use HTMX

- **Highly Dynamic Interfaces**: For applications requiring rapid and dynamic updates, such as online games or interactive spreadsheets, HTMX might not be the optimal solution.
- **Performance Concerns**: In situations where every millisecond counts, traditional JavaScript approaches might be preferable for achieving the highest performance.

## Conclusion

HTMX offers a viable alternative to SPAs for many use cases, balancing performance, simplicity, and scalability. It positions itself as a valuable tool for modern web developers, with successful case studies and clear recommendations. HTMX simplifies the development of interactive and responsive user interfaces, enabling developers to leverage the full potential of hypermedia with ease. Its adoption highlights a shift towards more efficient, maintainable, and accessible web applications, demonstrating the enduring relevance of hypermedia principles in today's digital landscape.

By embracing HTMX, developers can create rich web experiences that are both powerful and user-friendly, without the overhead and complexity often associated with SPAs. Whether you're building a simple informational site or a complex web application, HTMX provides the tools to make your web projects more dynamic, interactive, and engaging. As the web continues to evolve, HTMX represents a step forward in the quest for simpler, more effective web development methodologies, proving that sometimes, the most advanced solutions are those that bring us back to the basics.


---

## Discussion

### Benefits of HTMX

1. **Ease of Use**: HTMX simplifies web development by allowing any element to make HTTP requests and respond to events without extensive JavaScript. This makes it particularly useful for internal tools and moderately dynamic websites.

2. **Enhanced HTML Capabilities**: HTMX extends HTML to support richer interactions by allowing elements to handle HTTP actions directly. This reduces the need to manage complex client-side logic traditionally handled by JavaScript frameworks.

3. **Integration with Other Tools**: While HTMX reduces the need for JavaScript, it is often used in conjunction with vanilla JS or frameworks like AlpineJS for specific dynamic interactions, offering flexibility in development.

### Challenges with Mobile Browsers

1. **Mobile Optimization Issues**: Mobile browsers optimize by suspending background tabs, which can interrupt HTMX's functionality. This leads to unpredictable behavior, like network interruptions and cache issues, which are less controllable compared to raw JavaScript.

2. **State Management**: Maintaining state across sessions in mobile environments can be problematic. HTMX might face issues like losing scroll position or state inconsistencies due to browser optimizations, requiring additional JS to handle these cases.

### Philosophical and Practical Considerations

1. **HATEOAS Principles**: HTMX's approach aligns with Hypermedia as the Engine of Application State (HATEOAS), promoting a return to principles where the server dictates state through hypermedia. This can simplify the backend but might necessitate a tighter integration between frontend and backend.

2. **Mixing Markup with Logic**: Some developers express concern over the mixing of logic and markup in HTMX. Traditional approaches advocate separating concerns, but HTMX embeds control logic within HTML attributes, which can lead to tightly coupled frontend and backend code.

3. **Performance and Scalability**: Concerns are raised about the performance implications of HTMX in high-latency or bandwidth-limited environments, such as mobile networks. The necessity of round-trip HTTP requests for every interaction can be a drawback compared to SPAs, which handle more logic on the client side.

### Use Cases and Adoption

1. **Prototype Development**: HTMX is praised for rapid prototyping, allowing developers to quickly build interactive applications without deep knowledge of JavaScript. It is particularly appreciated by those less familiar with frontend development.

2. **Hybrid Approaches**: Many developers advocate for a hybrid approach, using HTMX for simple interactions and JavaScript frameworks like React or Vue for more complex, stateful interactions. This flexibility allows leveraging the strengths of both paradigms.

3. **Learning and Documentation**: The community highlights the availability of resources, such as the "Hypermedia Systems" book, which provides a comprehensive understanding of HTMX and hypermedia principles. The book is available for free online, supporting the learning curve for new adopters.

### Community Feedback

1. **Positive Experiences**: Many users report positive experiences with HTMX, appreciating its simplicity and how it "just works" for their needs. It allows them to focus more on solving problems rather than managing complex toolchains.

2. **Critical Feedback**: Others point out scenarios where HTMX might not be the best fit, such as highly interactive SPAs or applications requiring extensive client-side state management. The need for backend developers to understand and manipulate frontend templates is also seen as a potential hurdle.

3. **Innovative Extensions**: Discussions also touch on extensions like Hyperscript, which offers an alternative to JavaScript for handling client-side logic in HTMX applications, though it is noted as speculative and not essential for HTMX use.

<!-- Keywords -->
#hypermedia #hypertext #html5 #html #webmasters
<!-- /Keywords -->
