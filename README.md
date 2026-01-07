# Abhishek Jha - Portfolio Website

[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue)](https://github.com/abhishek-jha/portfolio)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modern, bilingual (English/German) portfolio website showcasing my work in autonomous vehicles, ROS2 development, and embedded systems.

## Features

- **Bilingual Support**: Seamlessly switch between English and German
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Fast Loading**: Lightweight and optimized for performance
- **GitHub Pages Ready**: Deployed and hosted on GitHub Pages

## Sections

1. **Hero/Home**: Introduction and quick links
2. **About**: Professional summary and key achievements
3. **Skills**: Technical skills organized by category
4. **Projects**: Showcase of 6 featured projects focusing on:
   - Autonomous Vehicle Prototype (ROS2)
   - Real-Time Vehicle Control Systems
   - CAN Integration Automation
   - Hyperloop Drive System
   - Test Bench Automation
   - Solar Module Analysis
5. **Experience**: Professional timeline with detailed work history
6. **Contact**: Multiple ways to get in touch

## Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS Grid, Flexbox, and animations
- **JavaScript**: Interactive features and language switching
- **Font Awesome**: Professional icons
- **Git**: Version control
- **GitHub Pages**: Hosting

## Setup Instructions

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/portfolio.git
   cd portfolio
   ```

2. **Open in browser**
   Simply open `index.html` in your web browser:
   - **Windows**: Double-click `index.html` or right-click > Open with > Browser
   - **Mac/Linux**: `open index.html` or drag to browser

3. **Local Server (Optional)**
   For better development experience, use a local server:

   Using Python:
   ```bash
   # Python 3
   python -m http.server 8000

   # Python 2
   python -m SimpleHTTPServer 8000
   ```

   Then open: `http://localhost:8000`

   Using Node.js (with `http-server`):
   ```bash
   npx http-server
   ```

   Using VS Code:
   - Install "Live Server" extension
   - Right-click `index.html` > "Open with Live Server"

## Deployment to GitHub Pages

### Method 1: GitHub Repository Settings (Recommended)

1. **Create a GitHub repository**
   ```bash
   # On GitHub, create a new repository named 'portfolio'
   ```

2. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/portfolio.git
   git add .
   git commit -m "Initial commit: Portfolio website"
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click "Settings" > "Pages"
   - Under "Source", select "main" branch
   - Click "Save"
   - Your site will be published at: `https://YOUR_USERNAME.github.io/portfolio/`

### Method 2: GitHub Pages Branch

1. **Create and deploy to gh-pages branch**
   ```bash
   git checkout -b gh-pages
   git push origin gh-pages
   ```

2. **Enable GitHub Pages**
   - Go to Settings > Pages
   - Select "gh-pages" branch
   - Your site will be live in a few minutes

### Method 3: Using as User/Organization Site

1. **Create a repository named**: `YOUR_USERNAME.github.io`

2. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

3. **Access your site** at: `https://YOUR_USERNAME.github.io`

## Customization

### Update Personal Information

1. **Contact Details** (index.html):
   - Email: Update `abjha1998@gmail.com`
   - Phone: Update `+49 1525 5867075`
   - LinkedIn: Update profile URL
   - Location: Update as needed

2. **Projects**:
   - Edit project cards in the "Projects Section" of `index.html`
   - Add/remove projects as needed
   - Update project descriptions and tags

3. **Experience**:
   - Update timeline items in the "Experience Section"
   - Add new positions or remove old ones

4. **Skills**:
   - Edit skill categories and tags in the "Skills Section"
   - Add or remove technical skills

### Styling Customization

Edit `css/styles.css` to customize:

- **Colors**: Modify CSS variables in `:root`
  ```css
  :root {
      --primary-color: #2563eb;
      --secondary-color: #1e40af;
      /* ... other colors */
  }
  ```

- **Fonts**: Change font families
- **Animations**: Adjust animation speeds and effects
- **Layout**: Modify grid layouts and spacing

### Adding New Language

To add a third language (e.g., Hindi):

1. Add language button in HTML:
   ```html
   <button onclick="switchLanguage('hi')" class="lang-btn" id="lang-hi">HI</button>
   ```

2. Add `data-hi` attributes to translatable elements:
   ```html
   <h1 data-en="About" data-de="Über mich" data-hi="के बारे में">About</h1>
   ```

3. Update `js/script.js` if needed

## Project Structure

```
portfolio/
│
├── index.html              # Main HTML file
├── README.md              # This file
├── LICENSE                # License file
│
├── css/
│   └── styles.css         # All styles
│
├── js/
│   └── script.js          # JavaScript functionality
│
├── images/                # Images folder (add your images here)
│   └── (your images)
│
└── assets/                # Additional assets
    └── (other files)
```

## Features in Detail

### Language Switching
- Toggle between English and German with a single click
- Language preference saved in localStorage
- Keyboard shortcut: Press 'L' to switch languages

### Responsive Design
- Mobile-first approach
- Hamburger menu on mobile devices
- Optimized layouts for all screen sizes

### Performance
- Minimal dependencies (only Font Awesome for icons)
- Optimized CSS with efficient selectors
- Lazy loading for animations
- Debounced scroll events

### Accessibility
- Semantic HTML5 markup
- ARIA labels for screen readers
- Keyboard navigation support
- High contrast text

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Opera (latest)

## Contributing

This is a personal portfolio, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

**Abhishek Jha**
- Email: abjha1998@gmail.com
- Phone: +49 1525 5867075
- LinkedIn: [abhishek-j-3497a8121](https://www.linkedin.com/in/abhishek-j-3497a8121)
- Location: Aachen, Germany

---

**Note**: Remember to replace `YOUR_USERNAME` with your actual GitHub username in all URLs and commands.

## Troubleshooting

### Site not loading on GitHub Pages
- Ensure the repository is public
- Check that GitHub Pages is enabled in Settings
- Wait a few minutes after enabling (initial deployment takes time)
- Clear browser cache

### Language switching not working
- Check browser console for JavaScript errors
- Ensure `js/script.js` is properly linked
- Verify `data-en` and `data-de` attributes are present

### Styles not applying
- Check that `css/styles.css` path is correct
- Verify file structure matches expected layout
- Clear browser cache

### Images not loading
- Ensure images are in the correct folder
- Use relative paths in HTML
- Check file names match exactly (case-sensitive)

## Future Enhancements

- [ ] Add dark mode toggle
- [ ] Integrate blog section
- [ ] Add project detail pages
- [ ] Include downloadable resume PDF
- [ ] Add contact form with backend
- [ ] Integrate Google Analytics
- [ ] Add more projects from GitHub API
- [ ] SEO optimization
- [ ] Performance optimization with lazy loading

---

Built with ❤️ for showcasing autonomous vehicle and ROS2 development work.
