import { Suspense } from 'react';
import LoginPage from '@/app/login/LoginPage';

export default function Page() {
  return (
    <Suspense>
      <LoginPage />
    </Suspense>
  );
}