Single Page Applications (SPAs) have gained popularity in web development for their ability to create fast, interactive, and responsive user experiences. At Abilian we've built several projects using Angular, Vue or React. However, we've become aware of the many drawbacks to using SPAs that developers should be aware of:

4.  **Complexity**: Developing and maintaining SPAs can be more complex than traditional multi-page applications. Developers need to manage state, deal with asynchronous data loading, and handle client-side rendering, which can lead to a steeper learning curve and increased development time. More specifically:

	1. **State management**: In SPAs, the state of the application is often maintained on the client side, which can become complex as the application grows. Developers need to manage the state of components, user interactions, and data fetched from the server. State management libraries like Redux (for React) or Vuex (for Vue) can help alleviate this complexity, but they introduce additional concepts and boilerplate code that developers need to learn and manage.
	
	2. **Asynchronous data loading**: SPAs rely on asynchronous data loading, which means data is fetched from the server on-demand as the user interacts with the application. This involves handling API calls, managing loading states, and handling errors. The asynchronous nature of these operations can lead to complex code structures and the need for managing promises or using async/await syntax.
	
	3. **Client-side rendering**: In SPAs, rendering is performed on the client side, which means developers need to understand and work with DOM manipulation, component lifecycle methods, and performance optimizations. This can be a steep learning curve for developers who are used to server-side rendering or those who are new to JavaScript.
	
	4. **Routing**: SPAs require client-side routing to handle navigation between different views or sections within the application. Developers need to learn and implement client-side routing libraries like React Router, Vue Router, or Angular Router. This adds complexity, as developers need to manage route configurations, route guards, and dynamic route generation.
	
	5. **Code splitting and lazy loading**: To optimize the performance of SPAs, developers often need to implement code splitting and lazy loading techniques to reduce the initial bundle size and load resources on-demand. This requires understanding of build tools like Webpack and managing dynamic imports in the code.
	
	6. **Testing**: Testing SPAs can be more complex than testing traditional MPAs, as developers need to test both the client-side and server-side code. This often involves setting up and configuring testing frameworks like Jest, Mocha, or Jasmine, as well as using testing utilities like React Testing Library or Angular TestBed.
	
	7. **Tooling and build process**: SPAs often require a build process and various development tools, such as bundlers (Webpack, Parcel, or Rollup), transpilers (Babel), and task runners (Gulp or Grunt). Developers need to understand and configure these tools, adding to the overall complexity and development time.

6.  **Initial load time**: Since SPAs load all the necessary resources and data during the initial page load, it can lead to longer initial load times, especially for large applications with many assets.
    
2.  **SEO challenges**: Search engines have improved in crawling and indexing JavaScript-heavy applications, but SPAs can still pose challenges for search engine optimization (SEO). This is because content is generated dynamically, which can make it more difficult for search engine bots to discover and index the site's content.
    
3.  **Limited browser history and navigation**: Traditional browser navigation features, such as the back button and bookmarks, can be difficult to implement in SPAs due to their dynamic nature. Developers need to manually manage the browser history and ensure that URLs are updated correctly to provide a seamless user experience.
    
5.  **JavaScript dependency**: SPAs rely heavily on JavaScript to function, and if a user has JavaScript disabled or if there's an issue with the JavaScript code, the application may not work as intended. This can create accessibility and usability issues for some users.
    
6.  **Poor performance on low-powered devices**: Since SPAs perform most of the processing on the client side, they can be resource-intensive, leading to poor performance on low-powered devices or slow internet connections.
    
7.  **Security concerns**: SPAs can be more vulnerable to security threats like Cross-Site Scripting (XSS) attacks since they execute more code on the client side. Developers need to be diligent in implementing proper security measures to protect user data and the application itself.
    
8.  **Difficulty in analytics tracking**: Traditional analytics tracking methods may not work well with SPAs, as page views are not triggered with each route change. Developers need to set up custom event tracking to accurately measure user interactions and engagement.

## Complexity: the main culprit

Most of these issues are technical, and can be solved, or mitigated, using technical solutions. However, the complexity inherent to SPAs has deep organizational issues and business drawbacks, impacting the development process, team collaboration, and overall project success. Some of these challenges include:

1. **Longer development time**: The complexity of SPAs can result in longer development time, as developers need to learn and manage various aspects of the application, such as state management, client-side rendering, and asynchronous data loading. This may delay the time-to-market for the application and increase development costs.

2. **Steeper learning curve**: The intricate nature of SPAs can lead to a steeper learning curve for new team members or developers who are not familiar with the SPA architecture or the specific JavaScript framework being used. This may require additional training and onboarding time, impacting the overall productivity of the team.

3. **Difficulties in hiring and retaining talent**: Due to the specialized skills required to develop and maintain SPAs, finding and retaining experienced developers can be challenging. This may lead to higher recruitment costs and potential delays in project timelines.

4. **Increased reliance on front-end developers**: The complexity of SPAs often requires a higher level of developer involvement in the decision-making process, as well as in ongoing maintenance and updates. This can create a bottleneck in the development process and increase the risk of project delays if key developers are unavailable or leave the company.

5. **Cross-team collaboration challenges**: The separation of concerns between the front-end and back-end in SPAs may lead to communication and collaboration issues between different teams or departments, particularly when it comes to API design and implementation.

6. **Difficulty in estimating project scope and budge**t: The complexity of SPAs can make it challenging to accurately estimate the project scope, timeline, and budget, potentially leading to cost overruns and missed deadlines.

7. **Technical debt and maintainability**: The intricate nature of SPAs can result in increased technical debt over time, especially if best practices are not followed, or if developers rely on outdated or poorly-maintained libraries. This can negatively impact the maintainability of the application and increase the cost of future updates and bug fixes.

8. **Scalability concerns**: As the application grows in size and complexity, the SPA architecture may become less efficient or difficult to scale, leading to performance issues or the need for significant refactoring efforts.

To mitigate these organizational issues and business drawbacks, we always carefully consider the specific needs of our project and those of our customers, and weigh the benefits and drawbacks of using SPAs before committing to this architecture, and we've deprioritized their use, favoring more lightweight approaches.


## What else then?

### HTMX

⇒ https://quii.dev/HTMX_is_the_Future

HTMX (formerly known as intercooler.js) is a small JavaScript library that enables developers to build modern, interactive web applications without the complexity of traditional front-end frameworks like React, Angular, or Vue. The library focuses on enhancing HTML by extending its syntax with custom attributes, allowing developers to achieve rich interactivity while maintaining a server-centric approach.

HTMX embraces the idea of "HTML over the wire," which means that, instead of sending JSON or other data formats, the server sends HTML fragments back to the client in response to user interactions. This allows developers to maintain most of their application logic on the server side and reduces the amount of JavaScript required on the client side, simplifying the development process.

Key features of HTMX include:

1. **AJAX and WebSockets support**: HTMX provides easy-to-use attributes for making AJAX requests and managing WebSocket connections. This enables real-time updates and asynchronous interactions without writing complex JavaScript code.

2. **Server-side rendering**: Since HTMX focuses on server-centric web applications, server-side rendering is the default approach, improving initial load times, SEO, and compatibility with non-JavaScript environments.

3. **Progressive enhancement**: HTMX enables progressive enhancement by design, allowing developers to start with basic HTML functionality and incrementally add interactivity as needed. This results in improved accessibility and user experience across different devices and connection speeds.

4. **Lightweight and unobtrusive**: With a small file size, HTMX has a minimal impact on page load times, and its unobtrusive approach allows developers to easily integrate it into existing projects without rewriting the entire application.

5. **No build step**: HTMX doesn't require a build step or complex tooling, which can streamline the development process and lower the barrier to entry for developers.

While HTMX is not as feature-rich as full-fledged front-end frameworks, it offers a simpler, more accessible way to build interactive web applications for developers who prefer to focus on server-side logic or those who are looking for an alternative to the SPA model. By adopting HTMX, we can leverage its simplicity and server-centric approach, which can help mitigate several issues:

1.  **Reduced development time**: HTMX allows developers to build interactive applications without the need for a comprehensive front-end framework, which can lead to faster development time and quicker time-to-market.
    
2. **Lower learning curve**: HTMX focuses on extending HTML with custom attributes, making it easier for developers to learn and understand, particularly for those with a strong background in HTML and server-side development.
    
3. **Easier hiring and onboarding**: Since HTMX is built on the familiar concepts of hypertext, it may be easier to find and onboard developers with the necessary skills to work with this library.
    
4. **Simplified cross-team collaboration**: HTMX promotes a server-centric approach, which can help bridge the gap between front-end and back-end teams and improve cross-team collaboration, particularly in the design and implementation of APIs and server-rendered HTML.
    
5. **Reduced reliance on front-end developers**: HTMX requires less specialized front-end knowledge, which means that the reliance on developers with specific expertise in front-end frameworks can be reduced, potentially speeding up the development process and decision-making.
    
6. **Improved maintainability and reduced technical debt**: The simplicity of HTMX and its focus on hypertext can help reduce technical debt and make the application easier to maintain and update over time.
    
However, it's important to note that HTMX may not be suitable for every project. Its simplicity comes with certain limitations, and it might not provide the same level of interactivity and performance optimizations as full-fledged front-end frameworks like React, Angular, or Vue, or some lightweight alternatives like AlpineJS. Additionally, HTMX may not be the best choice for applications with complex client-side logic, as it is primarily designed for server-driven applications.
