Frontend Developer Guide
=======================

Getting started
- Enter the `frontend/` directory and install dependencies: `npm install`.
- Start dev server: `npm run dev` (uses Vite).

Build
- Build production bundle: `npm run build`.

Integration
- The frontend communicates with the backend API. Set `VITE_API_URL` (or `APP_URL`) in the environment for API base URL.

Testing
- Use `npm test` if tests are added; ensure backend is running for end-to-end flows.

Style
- Use Tailwind utilities present in `frontend/src/styles.css` and follow existing component patterns.
