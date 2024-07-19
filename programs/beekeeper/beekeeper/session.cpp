#include <beekeeper/session.hpp>

#include <core/beekeeper_instance_base.hpp>

#include <appbase/application.hpp>

namespace beekeeper {

session::session( const std::string& token, std::shared_ptr<time_manager_base> time, const boost::filesystem::path& wallet_directory )
        : session_base( token, time, wallet_directory )
{
}

} //beekeeper
