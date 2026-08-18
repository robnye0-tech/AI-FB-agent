import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Steadyline Dashboard",
  description: "Manage your Steadyline AI phone & text answering service.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
