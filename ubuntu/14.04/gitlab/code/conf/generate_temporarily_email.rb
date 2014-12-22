module Gitlab
  module OAuth
    class AuthHash
      def generate_temporarily_email
        "#{username}@example.co.jp"
      end
    end
  end
end
