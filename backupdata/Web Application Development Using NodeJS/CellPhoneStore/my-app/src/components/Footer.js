import React from "react";

const Footer = () => {
    return (
        <footer
            className="text-center text-lg-start text-white"
            style={{ backgroundColor: "#1c2331" }}
        >
            <section>
                <div className="container text-center text-md-start mt-5">
                    <div className="row mt-3">
                        <div className="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold">
                                Company name
                            </h6>
                            <hr
                                className="mb-4 mt-0 d-inline-block mx-auto"
                                style={{
                                    width: "60px",
                                    backgroundColor: "#7c4dff",
                                    height: "2px",
                                }} // Chuyển đổi style sang đối tượng
                            />
                            <p>
                                Here you can use rows and columns to organize
                                your footer content. Lorem ipsum dolor sit amet,
                                consectetur adipisicing elit.
                            </p>
                        </div>

                        <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold">Products</h6>
                            <hr
                                className="mb-4 mt-0 d-inline-block mx-auto"
                                style={{
                                    width: "60px",
                                    backgroundColor: "#7c4dff",
                                    height: "2px",
                                }} // Chuyển đổi style sang đối tượng
                            />
                            <p>
                                <a href="#!" className="text-white">
                                    MDBootstrap
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    MDWordPress
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    BrandFlow
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    Bootstrap Angular
                                </a>
                            </p>
                        </div>

                        <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
                            <h6 className="text-uppercase fw-bold">
                                Useful links
                            </h6>
                            <hr
                                className="mb-4 mt-0 d-inline-block mx-auto"
                                style={{
                                    width: "60px",
                                    backgroundColor: "#7c4dff",
                                    height: "2px",
                                }} // Chuyển đổi style sang đối tượng
                            />
                            <p>
                                <a href="#!" className="text-white">
                                    Your Account
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    Become an Affiliate
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    Shipping Rates
                                </a>
                            </p>
                            <p>
                                <a href="#!" className="text-white">
                                    Help
                                </a>
                            </p>
                        </div>

                        <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
                            <h6 className="text-uppercase fw-bold">Contact</h6>
                            <hr
                                className="mb-4 mt-0 d-inline-block mx-auto"
                                style={{
                                    width: "60px",
                                    backgroundColor: "#7c4dff",
                                    height: "2px",
                                }} // Chuyển đổi style sang đối tượng
                            />
                            <p>
                                <i className="fas fa-home mr-3"></i> New York,
                                NY 10012, US
                            </p>
                            <p>
                                <i className="fas fa-envelope mr-3"></i>{" "}
                                info@example.com
                            </p>
                            <p>
                                <i className="fas fa-phone mr-3"></i> + 01 234
                                567 88
                            </p>
                            <p>
                                <i className="fas fa-print mr-3"></i> + 01 234
                                567 89
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <div
                className="text-center p-3"
                style={{ backgroundColor: "rgba(0, 0, 0, 0.2)" }} // Chuyển đổi style sang đối tượng
            >
                © 2020 Copyright:
                <a className="text-white" href="https://mdbootstrap.com/">
                    MDBootstrap.com
                </a>
            </div>
        </footer>
    );
};

export default Footer;
