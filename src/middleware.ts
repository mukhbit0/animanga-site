import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware((context, next) => {
  const runtime = context.locals.runtime;
  if (runtime && runtime.env) {
    (globalThis as any).currentEnv = runtime.env;
  }
  return next();
});
