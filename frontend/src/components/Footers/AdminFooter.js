const Footer = () => {
  return (
    <footer className="bg-light footer position-fixed bottom-0 w-100">
          <div className="copyright text-center text-xl-left text-muted">
            © {new Date().getFullYear()}{" "}
            <a
              className="font-weight-bold ml-1 text-black-50"
              href="https://www.linkedin.com/in/anis-ben-houidi/"
              rel="noopener noreferrer"
              target="_blank"
            >
              Anis Ben Houidi
            </a>
          </div>
    </footer>
  );
};
export default Footer;
