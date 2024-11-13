
https://innovation.ebayinc.com/tech/engineering/how-our-css-framework-helps-enforce-accessibility/

The article "How Our CSS Framework Helps Enforce Accessibility" by Ian McBurnie focuses on the importance of ensuring that user interface (UI) elements not only appear correctly but are also semantically described for accessibility purposes.

1. **Correct Use of Semantics**: UI elements like buttons must be identified with appropriate HTML tags (e.g., `<button>`) or roles (e.g., `role="button"`). This ensures that assistive technologies (AT), such as screen readers, can properly describe the element's function to users who rely on them.

2. **Accessibility Tree**: Screen readers rely on the accessibility tree, which is built from the HTML structure. If incorrect elements, like `<span>` instead of `<button>`, are used to create buttons, AT cannot recognize them, thus failing to provide essential interaction cues (e.g., how to activate a button).

3. **CSS Frameworks as a Layer of Defense**: CSS frameworks can enforce accessibility by using attribute selectors to require correct HTML markup before applying styles. For example, styling a button with `[role=button]` ensures that only elements semantically defined as buttons receive the correct visual treatment.

4. **Avoiding 'Fake' Buttons**: Styling non-semantic elements (e.g., `<span>` or `<div>`) as buttons without proper ARIA roles and behaviors is problematic. Developers should use real button elements wherever possible since they inherit essential behaviors like keyboard interaction (e.g., using SPACE or ENTER to activate the button).

5. **Swiss Cheese Model of Defense**: The author likens accessibility best practices to the Swiss cheese model, where multiple defenses (e.g., code linting, code reviews, accessibility checkers) must be layered to mitigate risks, as each layer may have flaws.

6. **State Enforcement with CSS**: CSS can also enforce the correct use of states, such as disabled buttons. Using the `[disabled]` attribute in CSS, rather than relying on class-based styles (e.g., `.btn--disabled`), ensures that buttons are semantically and functionally disabled for all users, including those using AT.

7. **ARIA and JavaScript for Complex Widgets**: ARIA (Accessible Rich Internet Applications) roles and states are necessary for more complex UI elements like tabs, menus, and carousels. ARIA can define roles such as `tablist`, `tab`, and `tabpanel` for a tabs widget, and CSS selectors can enforce these roles and states to ensure accessible design.

8. **Progressive Enhancement and Accessible Behavior**: Progressive enhancement ensures that even if JavaScript is disabled, core functionality remains. For instance, links can be used as fallback anchors in tab controls, and only when JavaScript is available do they become dynamic tabs. Additionally, ARIA states like `aria-selected` and `aria-hidden` can be used with JavaScript to manage focus and visibility dynamically.

9. **Key Takeaway**: CSS, HTML, and ARIA roles should be used together to ensure accessibility. When designing, developers should think about leveraging ARIA and HTML attributes instead of relying solely on custom classes (e.g., `.active`, `.hidden`, `.on`) for accessibility. The ultimate goal is to create controls that are both visually and functionally accessible.

10. **Future of the CSS Framework**: The author hints at an upcoming open-source release of the CSS framework that enforces these accessibility practices.

<!-- Keywords -->
#css #html #markup
<!-- /Keywords -->
