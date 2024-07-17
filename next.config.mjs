/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/api/:path*"
            : "https://anki-converter.zenathra.com/api/:path*",
        headers:
          process.env.NODE_ENV !== "development"
            ? { "X-Forwarded-Host": "nextjs" }
            : {},
      },
    ];
  },
};

export default nextConfig;
